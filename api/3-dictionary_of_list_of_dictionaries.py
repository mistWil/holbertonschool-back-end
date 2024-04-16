#!/usr/bin/python3


"""Dictionary of list of dictionaries"""


import json
import urllib.request


def export_to_json():
    # API endpoint URL for users
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Send GET request to the API for users
    with urllib.request.urlopen(users_url) as response:
        # Check if the request was successful
        if response.status == 200:
            # Get the JSON data from the response
            users = json.loads(response.read().decode())

            # Create a dictionary to store the tasks for all users
            all_tasks = {}

            # Iterate over each user
            for user in users:
                user_id = str(user["id"])
                username = user["username"]

                # API endpoint URL for user's tasks
                base_url = "https://jsonplaceholder.typicode.com/users/"
                tasks_url = base_url + f"{user_id}/todos"

                # Send GET request to the API for user's tasks
                with urllib.request.urlopen(tasks_url) as response:
                    # Check if the request was successful
                    if response.status == 200:
                        # Get the JSON data from the response
                        todos = json.loads(response.read().decode())

                        # Create a list of dictionaries for the user's tasks
                        user_tasks = [
                            {
                                "username": username,
                                "task": task["title"],
                                "completed": task["completed"]
                            } for task in todos
                        ]

                        # Add the user's tasks to the all_tasks dictionary
                        all_tasks[user_id] = user_tasks

            # Create a JSON file with all tasks for all employees
            filename = "todo_all_employees.json"
            with open(filename, mode='w') as file:
                json.dump(all_tasks, file)

            print(f"Data exported to {filename}")
        else:
            print(f"Error: {response.status}")


if __name__ == "__main__":
    export_to_json()
