#!/usr/bin/python3
"""
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    """prints the requested info"""

    Id = int(argv[1])
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(Id)).json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(Id)).json()
    with open('{}.csv'.format(Id), 'w') as f:
        csv_file = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            csv_file.writerow(
                [Id, employee['name'], task['completed'], task['title']])
