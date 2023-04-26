#!/usr/bin/python3
"""API module"""
import json
import requests


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    resp1 = requests.get('{}/users'.format(api_url))
    employees = resp1.json()
    data = {}
    for employee in employees:
        tasks_list = []
        data[employee.get('id')] = tasks_list
        resp2 = requests.get('{}/todos?userId={}'.format(
            api_url,
            employee.get('id')
        ))
        tasks = resp2.json()
        for task in tasks:
            tasks_list.append({
                "username": employee.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })
    with open('todo_all_employees.json', 'w') as file_:
        json.dump(data, file_)
