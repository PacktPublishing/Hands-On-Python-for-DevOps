from todoist_api_python.api import TodoistAPI
import json
from datetime import datetime, timezone
import requests

api = TodoistAPI("<your_api_token_here>")
access_token = "<Your_Microsoft_token_here>"

#Endpoint for your default task list
TODO_API_ENDPOINT = 'https://graph.microsoft.com/v1.0/me/todo/lists/@default/tasks'

def create_todo_task(title,date):
    headers = {
        'Authorization': 'Bearer '+access_token,
        'Content-Type': 'application/json'
    }

    payload = {
        'title': title,
        'dueDateTime': date
    }

    response = requests.post(TODO_API_ENDPOINT, headers=headers, json=payload)
    return response.json() if response.status_code == 201 else None

try:
    tasks = json.dumps(api.get_tasks(),default=lambda o: o.__dict__,sort_keys=True, indent=4)
    for task in tasks:
        title = task["content"]
        date = task["due"]["date"].replace(tzinfo=timezone.utc).astimezone(tz=None)
        create_todo_task(title, date)
except Exception as error:
    print(error)
