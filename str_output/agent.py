from google.adk.agents.llm_agent import LlmAgent

from pydantic import BaseModel, Field
from datetime import date

class ToDoSchema(BaseModel):
    """Blueprint for email outputs"""
    task: str = Field(description="Task name")
    due_date: date = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name="todo_agent",
    instruction='''Generate todo items in exact JSON format,
    Make sure the format is strictly followed.
    Below is the fields you need to generate:
    1. task: Task name
    2. due_date: Due date in YYYY-MM-DD format
    3. priority: Priority of the task (low/medium/high)
    example output:
    {
        "task": "Call client",
        "due_date": "2023-10-10",
        "priority": "high"
    }
    ''',
    output_schema=ToDoSchema,
    output_key="todo"
) 
