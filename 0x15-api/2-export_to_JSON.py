#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
"""

import json
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Script that returns progress of a TODO list based on employee ID
        Args:
            employee_id (int): employees designated id
    """
    # find the employee name from /users/
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']
    name = user_data['username']

    # find todo details
    uuid = employee_id
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(uuid)
    response = requests.get(url)
    todos = response.json()

    # Filtecat 2.jsonr completed tasks
    completed_tasks = []
    for todo in todos:
        task_info = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": name
                }
        completed_tasks.append(task_info)

    # Create JSON object
    json_data = {str(employee_id): completed_tasks}

    # Write JSON data to file
    file_name = f"{employee_id}.json"
    with open(file_name, "w") as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    """Handle command line arguments"""
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list_progress(employee_id)
    except ValueError:
        pass
