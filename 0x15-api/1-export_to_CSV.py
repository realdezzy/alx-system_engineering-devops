#!/usr/bin/python3
""" Gather data """
import requests
import csv
from sys import argv


def get_data():
    """ Gather data from an API and add to csv"""

    filename = '{}.csv'.format(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()

    name = user['username']

    data = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()

    mycsv = csv.writer(open(filename, 'w'), quoting=csv.QUOTE_ALL)

    for row in data:
        mycsv.writerow([argv[1], name, row['completed'], row['title']])


if __name__ == '__main__':
    get_data()
