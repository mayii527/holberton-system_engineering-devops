#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to
export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    id_user = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todos_users = 'https://jsonplaceholder.typicode.com/todos?userId='
    try:
        if int(id_user):
            dict_user = requests.get(url_user + id_user).json()
            nameEmployee = dict_user.get('username')
            dict_todos_users = requests.get(url_todos_users + id_user).json()

            data_user = []
            for i in dict_todos_users:
                print('hello')
                data_user.append(i)

            print_data = []
            for a in data_user:
                data_user.append(id_user, nameEmployee,
                                 a['completed'], a['title'])

            with open('file.csv'.format(id_user), 'w', newline='') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
                writer.writerows(print_data)
    except:
        print('Error')
