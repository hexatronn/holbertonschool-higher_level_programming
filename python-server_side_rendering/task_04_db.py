#!/usr/bin/python3
"""
task_04_db.py
Read products from JSON, CSV, or SQLite and display using the same template.
"""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filename='products.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data if isinstance(data, list) else []


def read_products_csv(filename='products.csv'):
    products = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
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


def read_products_sql(db_path='products.db'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, name, category, price FROM Products")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source", products=[])

    try:
        if source == 'json':
            products_list = read_products_json()
        elif source == 'csv':
            products_list = read_products_csv()
        else:
            products_list = read_products_sql()
    except (OSError, json.JSONDecodeError, sqlite3.Error) as e:
        return render_template('product_display.html', error=f"Data source error: {e}", products=[])

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

    return render_template('product_display.html', error=None, products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
