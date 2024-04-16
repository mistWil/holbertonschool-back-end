#!/usr/bin/python3


"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress and exports data in CSV format."""


import csv
import requests
import sys


def export_to_csv(employee_id):
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

            # Sort tasks by completion status
            todos.sort(key=lambda x: (x["completed"], x["title"]))

            all_tasks = []

            # Create a list of lists with the required data
            for task in todos:
                task_completed_status = str(task["completed"])
                full_name = (
                    employee_name.split()[0] + " " +
                    employee_name.split()[1]
                )
                task_data = [
                    employee_id,
                    full_name,
                    task_completed_status.capitalize(),
                    task["title"]
                            ]
                all_tasks.append(task_data)

            # Write the data to a CSV file
            with open(f"{sys.argv[1]}.csv", 'w', encoding='utf8',
                      newline='') as f:
                csv_list = csv.writer(f, quoting=csv.QUOTE_ALL)
                csv_list.writerow(["USER_ID",
                                   "USERNAME",
                                   "TASK_COMPLETED_STATUS",
                                   "TASK_TITLE"])
                csv_list.writerows(all_tasks)

            print(f"Data exported to {sys.argv[1]}.csv")
        else:
            print(f"Error: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
