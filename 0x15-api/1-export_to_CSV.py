#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import csv
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    todo_url = url + "/user/{}/todos".format(employee_id)
    user_url = url + "/users/{}".format(employee_id)

    user_response = requests.get(user_url)
    username = user_response.json().get('username')

    todo_response = requests.get(todo_url)
    todo_json = todo_response.json()

    with open(f"{employee_id}.csv", "w") as file:
        write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todo_json:
            write.writerow([employee_id, username, todo.get('completed'),
                            todo.get('title')])
