import uuid
from typing import List, Dict, Any

class Task:
    def __init__(self, name: str, task_type: str, prompt_template: str = None):
        self.name = name
        self.task_type = task_type  # "llm" or "tool"
        self.prompt_template = prompt_template
        self.next_task = None

    def then(self, task):
        self.next_task = task.name
        return task

class AgentWorkflow:
    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}
        self.entry_task: str = None

    def add_task(self, task: Task):
        self.tasks[task.name] = task
        if not self.entry_task:
            self.entry_task = task.name
        return task

    def export_graph(self):
        """Compiles the workflow into a dictionary for the orchestrator."""
        return {
            "workflow_id": str(uuid.uuid4()),
            "tasks": {
                name: {
                    "type": t.task_type,
                    "prompt": t.prompt_template,
                    "next": t.next_task
                } for name, t in self.tasks.items()
            },
            "entry": self.entry_task
        }