#!/usr/bin/python3
"""
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """prints the requested info"""

    Id = int(argv[1])
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(Id)).json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(Id)).json()
    done_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?'
        'userId={}&&completed=true'.format(Id)).json()

    print("Employee {} is done with tasks({}/{}):".format(
        employee['name'], len(done_tasks), len(all_tasks)))
    [print("\t {}".format(task['title'])) for task in done_tasks]
