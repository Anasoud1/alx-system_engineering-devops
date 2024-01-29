#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    todo_url = url + '/todos'
    user_url = url + '/users'

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_json = todo_response.json()
    users = user_response.json()

    dic = {}

    with open("todo_all_employees.json", "w") as file:
        for user in users:
            list_dic = []
            for todo in todo_json:
                list_dic.append(
                    {
                        'username': user.get('username'),
                        'task': todo.get('title'),
                        'completed': todo.get('completed'),
                    })
            dic[user.get('id')] = list_dic
        json.dump(dic, file)
