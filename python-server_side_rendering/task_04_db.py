import sqlite3
import json
import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_sql():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    products = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        error = "Wrong source"
        products = []

    if product_id and not error:
        products = [p for p in products if str(p.get('id')) == str(product_id)]
        if not products:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)