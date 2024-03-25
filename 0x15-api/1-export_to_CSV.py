#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
Extended to export data in the CVS format
"""

import csv
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

    # No erros found , execute code
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed'] is True]
    num_completed_tasks = len(completed_tasks)


    # Export data in the CVS format
    f = "{}.csv".format(uuid)
    with open(f, mode="w", newline="") as file:
        writer = csv.writer(file)
        for todo in todos:
            writer.writerow([uuid, name, todo['completed'], todo['title']])


if __name__ == "__main__":
    """Handle command line arguments"""
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list_progress(employee_id)
    except ValueError:
        pass
