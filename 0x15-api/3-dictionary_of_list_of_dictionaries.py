#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
"""

import json
import requests
import sys


def fetch_todo_list_progress():
    """
    Script that returns progress of a TODO list for all employees
    """
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Initialize dictionary to store todos for all employees
    all_todos = {}

    # Iterate over each user to fetch their todos
    for user_data in users_data:
        employee_id = user_data['id']
        employee_name = user_data['name']
        username = user_data['username']

        # Fetch todos for current employee
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Filter completed tasks
        completed_tasks = []
        for todo in todos:
            task_info = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            completed_tasks.append(task_info)

        # Add todos to dictionary for all employees
        all_todos[str(employee_id)] = completed_tasks

    # Write all todos to a single JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(all_todos, file)


if __name__ == "__main__":
    fetch_todo_list_progress()
