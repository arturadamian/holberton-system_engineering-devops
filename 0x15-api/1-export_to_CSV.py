#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """
    Records all tasks that are owned by this employee
    """
    Id = int(argv[1])
    emp_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(Id)).json().get("username")
    all_tasks = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos?userId={}".format(Id)).json()
    with open("{}.csv".format(Id), "w") as fd:
        fill = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            fill.writerow([Id, emp_name,
                           task.get("completed"), task.get("title")])
