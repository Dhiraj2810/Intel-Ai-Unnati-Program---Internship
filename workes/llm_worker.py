import json
from kafka import KafkaConsumer, KafkaProducer
from optimum.intel import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline

# Configuration
MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Laptop friendly model
DEVICE = "CPU" # Change to "GPU" if you have Intel Iris Xe

print(f"⏳ Loading Intel OpenVINO Model: {MODEL_ID} on {DEVICE}...")
# Export=True converts the PyTorch model to OpenVINO format on first run
model = OVModelForCausalLM.from_pretrained(MODEL_ID, export=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model.to(DEVICE)
print("✅ Model Loaded!")

# Kafka Setup
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
consumer = KafkaConsumer('task_llm', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for msg in consumer:
    data = msg.value
    print(f"[LLM Worker] Processing: {data['task_name']}")
    
    # Construct Prompt
    prompt_template = data['definition']['prompt']
    user_input = data['context']
    full_prompt = f"<|system|>You are a helpful assistant.</s><|user|>{prompt_template.format(input=user_input)}</s><|assistant|>"
    
    # Inference
    inputs = tokenizer(full_prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Clean response (remove prompt echo if needed)
    final_output = response.split("<|assistant|>")[-1].strip()

    # Send back to Orchestrator (Input Loopback)
    producer.send('agent_ingress', {
        "workflow_id": data['workflow_id'],
        "task_name": data['task_name'],
        "result": final_output
    })