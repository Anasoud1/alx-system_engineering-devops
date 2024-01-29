#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    todo_url = url + "/todos"
    user_url = url + "/users/{}".format(employee_id)

    user_response = requests.get(user_url)
    user_json = user_response.json()

    todo_response = requests.get(todo_url, params={"userId": employee_id})
    todo_json = todo_response.json()
    done = 0
    all_todo = len(todo_json)

    for todo in todo_json:
        if todo.get("completed") is True:
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(user_json.get('name'),
          done, all_todo))

    for todo in todo_json:
        if todo.get("completed") is True:
            print("\t {}".format(todo.get('title')))
