#!/usr/bin/python3
"""
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

def get_employee():
    """prints the requested info"""

    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(argv[1])).json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(argv[1])).json()
    done_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?'
        'userId={}&&completed=true'.format(argv[1])).json()
    try:
        print("Employee {} is done with tasks({}/{}):".format(
            employee['name'], len(done_tasks), len(all_tasks)))
        [print("\t {}".format(task['title'])) for task in done_tasks]
    except:
        pass
if __name__ == "__main__":
    get_employee()
