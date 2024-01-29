#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import json
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    todo_url = url + '/users/{}/todos'.format(employee_id)
    user_url = url + '/users/{}'.format(employee_id)

    todo_response = requests.Session().get(todo_url)
    user_response = requests.Session().get(user_url)

    todo_json = todo_response.json()
    user = user_response.json().get('username')

    list_dic = []
    dic = {}

    with open(f"{employee_id}.json", "w") as file:
        for todo in todo_json:
            list_dic.append(
                    {
                        'task': todo.get('title'),
                        'completed': todo.get('completed'),
                        'username': user,
                    })
        dic[employee_id] = list_dic
        json.dump(dic, file)
