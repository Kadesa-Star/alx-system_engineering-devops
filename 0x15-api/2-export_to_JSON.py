#!/usr/bin/python3
"""
A script to fetch and export TODO list data for an employee to a JSON file.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetches TODO data for a given employee and exports it to a JSON file.

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

    # Prepare data for JSON export
    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos_data
        ]
    }

    # Define JSON filename
    filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_to_json(emp_id)
