#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
"""

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

    # find todo details
    uuid = employee_id
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(uuid)
    response = requests.get(url)
    todos = response.json()

    # No erros found , execute code
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed'] is True]
    num_completed_tasks = len(completed_tasks)

    # print output
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          num_completed_tasks,
                                                          total_tasks))
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    """Handle command line arguments"""
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list_progress(employee_id)
    except ValueError:
        pass
