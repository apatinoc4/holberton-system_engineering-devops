#!/usr/bin/python3
"""  returns information about his/her TODO list progress """
import requests
import sys
if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1]).json()
    tds = requests.get('https://jsonplaceholder.typicode.com/todos/?userId=' +
                       sys.argv[1]).json()
    name = users.get('name')
    total, done = 0, 0
    for todo in tds:
        total += 1
        if todo.get("completed"):
            done += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, done, total))
    for todo in tds:
        if todo.get("completed"):
            print("\t" + " " + todo.get("title"))
