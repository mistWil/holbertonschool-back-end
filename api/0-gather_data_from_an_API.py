#!/usr/bin/python3


"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""


import sys
import requests


def get_employee_todo_progress(employee_id):
    # API endpoint URL for employee information
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Send GET request to the API for employee information
    response = requests.get(employee_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        employee_data = response.json()

        # Get the employee name
        employee_name = employee_data["name"]

        # API endpoint URL for employee's tasks
        base_url = "https://jsonplaceholder.typicode.com/users/"
        tasks_url = base_url + f"{employee_id}/todos"

        # Send GET request to the API for employee's tasks
        response = requests.get(tasks_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON data from the response
            todos = response.json()

            # Count the number of completed and total tasks
            completed_tasks = [todo for todo in todos if todo["completed"]]
            total_tasks = len(todos)
            num_completed_tasks = len(completed_tasks)

            # Print the employee TODO list progress
            employee_message = f"Employee {employee_name} is done with"
            tasks_count = f"tasks({num_completed_tasks}/{total_tasks})"
            print(employee_message + " " + tasks_count + ":")

            # Print the titles of completed tasks
            for task in reversed(completed_tasks):
                print(f"\t {task['title']}")
        else:
            print(f"Error: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
