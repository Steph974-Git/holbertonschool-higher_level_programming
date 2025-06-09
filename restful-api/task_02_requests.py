#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        data = r.json()

        for post in data:
            print(post['title'])

def fetch_and_save_posts():

    