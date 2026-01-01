import json
from kafka import KafkaConsumer, KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
consumer = KafkaConsumer('task_tool', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print(">>> Tool Worker Started.")

for msg in consumer:
    data = msg.value
    print(f"[Tool Worker] Executing: {data['task_name']}")
    
    # Simple Mock Tool Logic
    input_data = data['context']
    result = f"Analyzed data for: {input_data}. Status: VALID."
    
    producer.send('agent_ingress', {
        "workflow_id": data['workflow_id'],
        "task_name": data['task_name'],
        "result": result
    })