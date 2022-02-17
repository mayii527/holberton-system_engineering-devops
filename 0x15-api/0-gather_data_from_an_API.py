#!/usr/bin/python3
"""
 using this REST API, for a given 
 employee ID, returns information 
 about his/her todo list progress.
"""
from time import process_time_ns
import requests
from sys import argv


if __name__ == "__main__":
    id_user = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todos_users = 'https://jsonplaceholder.typicode.com/todos?userId='
    dict_user = requests.get(url_user + id_user).json()
    nameEmployee = dict_user.get('name')
    dict_todos_users = requests.get(url_todos_users + id_user).json()
    all_tasks = len(dict_todos_users)
    done_tasks = []
    for i in dict_todos_users:
        if i.get('completed') is True:
            done_tasks.append(i.get('title'))
            len(done_tasks)
    print('Employee {} is done with tasks({}/{}):'.format(nameEmployee,len(done_tasks),all_tasks))
    for tasks in done_tasks:
        print('\t {}'.format(tasks))
