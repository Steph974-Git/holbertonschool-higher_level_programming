#!/usr/bin/env python3

import requests
import csv

def fetch_and_print_posts():

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        data = r.json()

        for post in data:
            print("{}".format(post['title']))

def fetch_and_save_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if r.status_code == 200:
        data= r.json()

        structured_posts = []
        for post in data:
            structured_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(structured_posts)

    print("Posts saved to posts.csv successfully")
        
if __name__ == "__main__":
    print("Fetching and printing posts:")
    fetch_and_print_posts()
            
    print("\nFetching and saving posts to CSV:")
    fetch_and_save_posts()
