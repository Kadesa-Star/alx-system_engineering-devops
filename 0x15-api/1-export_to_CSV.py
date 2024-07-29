#!/usr/bin/python3
"""
A script to fetch and export TODO list data for an employee to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Fetches TODO data for a given employee and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee to fetch data for.
    """
    # Define API endpoints
    users_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?"
        f"userId={employee_id}"
    )

    # Fetch employee data
    user_response = requests.get(users_url)
    user_data = user_response.json()
    username = user_data.get("username", "Unknown")

    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Define CSV filename
    filename = f"{employee_id}.csv"

    # Write data to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            user_id = task.get('userId')
            task_title = task.get('title')
            task_completed = task.get('completed')
            csv_writer.writerow(
                    [user_id, username, task_completed, task_title]
                    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_to_csv(emp_id)
