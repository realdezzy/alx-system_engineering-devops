#!/usr/bin/python3
"""API module"""
import json
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    resp1 = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = resp1.json().get('username')
    resp2 = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = resp2.json()
    with open('{}.json'.format(employee_id), 'w') as file_:
        tasks_list = []
        data = {employee_id: tasks_list}
        for resp in responses:
            tasks_list.append({
                "task": resp.get('title'),
                "completed": resp.get('completed'),
                "username": employee_username
            })
        json.dump(data, file_)
