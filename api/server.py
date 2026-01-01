from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka import KafkaProducer
from framework.sdk import AgentWorkflow, Task
import json
import uuid

app = FastAPI(title="IntelAgentCore Gateway")

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class WorkflowRequest(BaseModel):
    agent_name: str
    user_input: str

@app.post("/api/run")
async def run_workflow(request: WorkflowRequest):
    workflow_id = str(uuid.uuid4())
    
    # Define Agent Workflows dynamically based on request
    # (In a real app, load these from a DB)
    if request.agent_name == "audit_bot":
        # Create the specific workflow graph
        wf = AgentWorkflow("Audit_Bot")
        t1 = Task("scan_code", "tool") # Calls Tool Worker
        t2 = Task("summarize", "llm", prompt_template="Summarize this security scan: {input}") # Calls LLM Worker
        wf.add_task(t1).then(t2)
        wf.add_task(t2)
        
        payload = wf.export_graph()
        payload['workflow_id'] = workflow_id
        payload['initial_input'] = request.user_input
        
        # Send to Orchestrator via Kafka
        producer.send('agent_ingress', payload)
        
        return {"status": "submitted", "workflow_id": workflow_id}
    
    else:
        raise HTTPException(status_code=404, detail="Agent not found")

@app.get("/")
def health_check():
    return {"status": "IntelAgentCore Gateway Online"}

# Run with: uvicorn api.server:app --reload --port 8000