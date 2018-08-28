#!/usr/bin/python3
"""
export data in the JSON format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """
    Records all tasks that are owned by this employee
    """

    Id = int(argv[1])
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(Id)).json()
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(Id)).json()
    with open("{}.csv".format(Id), "w") as f:
        c_f = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            c_f.writerow(
                [Id, employee['name'], task['completed'], task['title']])
