#!/usr/bin/python3


"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""


import sys
import requests


def get_employee_todo_progress(employee_id):
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        todos = response.json()

        # Count the number of completed and total tasks
        completed_tasks = [todo for todo in todos if todo["completed"]]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)

        # Get the employee name
        employee_name = todos[0]["title"].split(" ")[0]

        # Print the employee TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

        # Print the titles of completed tasks
        for task in reversed(completed_tasks):
            print(f"\t {task['title']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)