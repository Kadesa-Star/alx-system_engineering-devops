#!/usr/bin/python3
"""
export data in the json format
Dictionary of list of dictionaries
"""

import json
import requests


def fetch_data():
    """Fetch data from API and return it."""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def transform_data(users, todos):
    """Transform data into the required format."""
    data = {}
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user['id']
        ]
        data[user_id] = user_tasks
    return data


def save_to_file(data):
    """Save transformed data to a JSON file."""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f, indent=4)


def main():
    """Main function to execute the script."""
    users, todos = fetch_data()
    data = transform_data(users, todos)
    save_to_file(data)


if __name__ == '__main__':
    main()
