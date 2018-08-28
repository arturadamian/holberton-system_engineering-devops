#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
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
    data = []
    js_file = {}

    for task in all_tasks:
        task_dct = {}
        task_dct["task"] = task["title"]
        task_dct["completed"] = task["completed"]
        task_dct["username"] = emp_name
        data.append(task_dct)
    js_file[Id] = data
    with open("{}.json".format(Id), 'w') as jsf:
        json.dump(js_file, jsf)
