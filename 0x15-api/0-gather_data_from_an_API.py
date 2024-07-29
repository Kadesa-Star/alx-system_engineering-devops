#!/usr/bin/python3
"""
A script to fetch and display TODO list progress for an employee
based on the provided employee ID.

The script uses JSONPlaceholder API to retrieve employee and TODO
data, then outputs the number of completed tasks and their titles
"""


import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch employee and TODO data, then display the TODO list progress.
    Args:
        employee_id (int): The ID of the employee to fetch data for
    """
    # Define API endpoints
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )

    # Fetch employee data
    user_response = requests.get(users_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate TODO progress
    total_tasks = len(todos_data)
    completed_tasks = (
            [task['title'] for task in todos_data if task.get('completed')]
            )
    num_done_tasks = len(completed_tasks)

    # output results
    print(
            f"Employee {employee_name} is done with tasks({num_done_tasks}/"
            f"{total_tasks}):"
        )
    for task in completed_tasks:
        print(f"    {task}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_data(emp_id)
