#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Records all tasks from all employees
    """
    js_dct = {}
    emp = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for item in emp:
        Id = item['id']
        all_tasks = requests.get("https://jsonplaceholder.typicode.com/"
                                 "todos?userId={}".format(Id)).json()
        task_dct = {}
        task_dct['username'] = item['name']
        js_lst = []
        for task in all_tasks:
            task_dct['completed'] = task['completed']
            task_dct["task"] = task["title"]
            js_lst.append(task_dct)
        js_dct[Id] = js_lst

    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(js_dct, jsf)
