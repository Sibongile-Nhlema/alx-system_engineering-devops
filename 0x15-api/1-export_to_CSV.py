#!/usr/bin/python3
"""
Script that returns progress of a TODO list based on employee ID
Extended to export data in the CVS format
"""

from gather_data_from_an_API import fetch_todo_list_progress
import csv
import requests
import sys


def export_todo_list_to_csv(employee_id):
    """
    Export the TODO list of an employee to a CSV file.
    Args:
        employee_id (int): Employee's designated id.
    """
    todos = fetch_todo_list_progress(employee_id)

    # Export data in the CSV format
    f = "{}.csv".format(employee_id)
    with open(f, mode="w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, todo['title'], todo['completed']])


if __name__ == "__main__":
    """Handle command line arguments"""
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_todo_list_to_csv(employee_id)
    except ValueError:
        pass
