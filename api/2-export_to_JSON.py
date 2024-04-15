#!/usr/bin/python3


"""Export to JSON"""


import sys
import urllib.request
import json


def export_to_json(employee_id):
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send GET request to the API
    with urllib.request.urlopen(url) as response:
        # Check if the request was successful
        if response.status == 200:
            # Get the JSON data from the response
            todos = json.loads(response.read().decode())

            # Get the employee name
            employee_name = todos[0]["title"].split(" ")[0]

            # Create a dictionary to store the tasks
            tasks_dict = {
                str(employee_id): [
                    {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": employee_name
                    } for task in todos
                ]
            }

            # Create a JSON file with the employee ID as the filename
            filename = f"{employee_id}.json"
            with open(filename, mode='w') as file:
                json.dump(tasks_dict, file)

            print(f"Data exported to {filename}")
        else:
            print(f"Error: {response.status}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
