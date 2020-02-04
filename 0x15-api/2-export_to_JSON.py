#!/usr/bin/python3
""" extend your Python script to export data in the JSON format. """
import json
import requests
import sys
if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1]).json()
    tds = requests.get('https://jsonplaceholder.typicode.com/todos/?userId=' +
                       sys.argv[1]).json()
    username = users.get('username')
    values = []
    for todo in tds:
        n_dict = {}
        n_dict["task"] = todo.get("title")
        n_dict["username"] = username
        n_dict["completed"] = todo.get("completed")
        values.append(n_dict)

    ids = {sys.argv[1]: values}
    with open(sys.argv[1] + '.json', 'w') as f:
                json.dump(ids, f)
