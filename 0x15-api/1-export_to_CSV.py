#!/usr/bin/python3
""" extend your Python script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1]).json()
    tds = requests.get('https://jsonplaceholder.typicode.com/todos/?userId=' +
                       sys.argv[1]).json()
    username = users.get('username')
    with open(sys.argv[1] + '.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in tds:
            writer.writerow([sys.argv[1], username, todo.get("completed"),
                            todo.get("title")])
