#!/usr/bin/python3
"""
task_02_logic.py
Flask app with Jinja logic (for/if) reading items from JSON
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    items_list = []

    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Expecting {"items": [...]} but stay safe:
            if isinstance(data, dict) and isinstance(data.get("items"), list):
                items_list = data["items"]
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error reading items.json: {e}")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
