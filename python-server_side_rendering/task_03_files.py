#!/usr/bin/python3
"""
task_03_files.py
Read products from JSON or CSV and display in a template.
"""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filename='products.json'):
    """Return a list of product dicts from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Expecting a list of dicts
    if not isinstance(data, list):
        return []
    return data


def read_products_csv(filename='products.csv'):
    """Return a list of product dicts from a CSV file."""
    products = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert types
            try:
                row["id"] = int(row.get("id"))
            except (TypeError, ValueError):
                row["id"] = None
            try:
                row["price"] = float(row.get("price"))
            except (TypeError, ValueError):
                row["price"] = 0.0
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)

    # Validate source
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source", products=[])

    # Read products
    try:
        if source == 'json':
            products_list = read_products_json()
        else:
            products_list = read_products_csv()
    except (OSError, json.JSONDecodeError) as e:
        return render_template('product_display.html', error=f"File error: {e}", products=[])

    # Filter by id if provided
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            return render_template('product_display.html', error="Product not found", products=[])

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        products_list = filtered

    return render_template('product_display.html', products=products_list, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
