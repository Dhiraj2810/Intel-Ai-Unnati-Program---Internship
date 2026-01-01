import json
from kafka import KafkaConsumer, KafkaProducer

# Kafka Config
KAFKA_SERVER = 'localhost:9092'
TOPIC_INGRESS = 'agent_ingress'
TOPIC_LLM = 'task_llm'
TOPIC_TOOL = 'task_tool'
TOPIC_COMPLETE = 'workflow_complete'

class Orchestrator:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.consumer = KafkaConsumer(
            TOPIC_INGRESS,
            bootstrap_servers=KAFKA_SERVER,
            group_id='orchestrator_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        # In-memory state storage (Use Redis/Cassandra for production)
        self.active_workflows = {} 

    def dispatch_task(self, workflow_id, task_name, context):
        workflow = self.active_workflows[workflow_id]['graph']
        task_def = workflow['tasks'][task_name]
        
        payload = {
            "workflow_id": workflow_id,
            "task_name": task_name,
            "context": context,
            "definition": task_def
        }

        if task_def['type'] == 'llm':
            print(f"[Orchestrator] Routing {task_name} to LLM Worker...")
            self.producer.send(TOPIC_LLM, payload)
        elif task_def['type'] == 'tool':
            print(f"[Orchestrator] Routing {task_name} to Tool Worker...")
            self.producer.send(TOPIC_TOOL, payload)

    def run(self):
        print(">>> Orchestrator Started. Waiting for workflows...")
        for message in self.consumer:
            data = message.value
            
            # Case 1: New Workflow Request
            if 'graph' in data:
                w_id = data['workflow_id']
                self.active_workflows[w_id] = {"graph": data, "history": []}
                print(f"[Orchestrator] Starting Workflow: {w_id}")
                self.dispatch_task(w_id, data['entry'], data['initial_input'])
            
            # Case 2: Task Result Received (Loopback)
            elif 'result' in data:
                w_id = data['workflow_id']
                finished_task = data['task_name']
                result = data['result']
                
                # Update State
                current_wf = self.active_workflows[w_id]['graph']
                next_task_name = current_wf['tasks'][finished_task]['next']
                
                if next_task_name:
                    # Continue Flow
                    self.dispatch_task(w_id, next_task_name, result)
                else:
                    # Workflow Finished
                    print(f"✅ [Orchestrator] Workflow {w_id} COMPLETE. Final Result: {result}")

if __name__ == "__main__":
    Orchestrator().run()