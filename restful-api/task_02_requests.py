#!/usr/bin/python3
"""
Fetches posts from JSONPlaceholder and prints titles
or saves selected data into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts and prints the response status and post titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves id, title, and body into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)
