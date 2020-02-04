#!/usr/bin/python3
""" extend your Python script to export data in the JSON format. """
import json
import requests
import sys
if __name__ == '__main__':
    f_dict = {}
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tds = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for user in users:
        username = user.get('username')
        vals = []
        for todo in tds:
            if todo.get('userId') == user.get('id'):
                n_dict = {}
                n_dict["task"] = todo.get("title")
                n_dict["username"] = username
                n_dict["completed"] = todo.get("completed")
                vals.append(n_dict)
        f_dict.update({user.get("id"): vals})
    with open('todo_all_employees.json', 'w') as f:
        json.dump(f_dict, f)
