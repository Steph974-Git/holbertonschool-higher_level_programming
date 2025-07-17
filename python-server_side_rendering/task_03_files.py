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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
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