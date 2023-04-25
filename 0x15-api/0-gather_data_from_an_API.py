#!/usr/bin/python3
""" Gather data """
import requests
from sys import argv


def get_data():
    """ Gather data from an API """
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    name = user['name']

    data = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    c = 0
    c = len([x for x in data if x['completed'] is True])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, c, len(data)))
    [print('\t {}'.format(x['title'])) for x in data if x['completed'] is True]


if __name__ == '__main__':
    get_data()
