#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
"""


import sys
import requests


def fetch_todo_list_progress(employee_id):
    """
    Script that returns progress of a TODO list based on employee ID
        Args:
            employee_id (int): employees designated id
    """
    uuid = employee_id
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(uuid)
    response = requests.get(url)
    todos = response.json()

    # Handle errors
    if response.status_code != 200:
        print("Failed: Could not fetch API data.")
        return

    # No erros found , execute code
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed'] == True]
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]['userId']

    # print output
    print("Employee {} is done with tasks ({}/{}):".format(employee_name,
                                                           num_completed_tasks,
                                                           total_tasks))
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    """Handle command line arguments"""
    if len(sys.argv) != 2:
        print("USAGE: Python3 0-gather_data_from_an_API.py <employee_ID>")
        sys.exit(1)
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an interger")
