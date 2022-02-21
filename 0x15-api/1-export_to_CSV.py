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
                data_user.append(i)

            print_data = []
            for a in data_user:
                print_data.append({'id': id_user, 'username': nameEmployee,
                                   'completed': str(a['completed']),
                                   'title': a['title']})

            fieldnames = ['id', 'username', 'completed', 'title']
            with open('{}.csv'.format(id_user), 'w',
                      encoding='UTF8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames,
                                        quoting=csv.QUOTE_ALL)
                for x in print_data:
                    writer.writerow(x)
    except ValueError:
        print('Error')
