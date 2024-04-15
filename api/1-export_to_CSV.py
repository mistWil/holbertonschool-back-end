#!/usr/bin/python3


"""Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""


import sys
import urllib.request
import json
import csv


def export_to_csv(employee_id):
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

            # Create a CSV file with the employee ID as the filename
            filename = f"{employee_id}.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)

                # Write the header row
                writer.writerow(["USER_ID", "USERNAME",
                                 "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                # Write each task as a row in the CSV file
                for task in todos:
                    task_completed_status = str(task["completed"]).lower()
                    writer.writerow([employee_id,
                                     employee_name,
                                     task_completed_status,
                                     task["title"]])

            print(f"Data exported to {filename}")
        else:
            print(f"Error: {response.status}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
