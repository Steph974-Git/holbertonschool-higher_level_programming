import json
import csv
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    with open('products.json') as f:
        data = json.load(f)
    product_id = request.args.get('id')
    if product_id is not None:
        filtered_data = [item for item in data if str(item.get("id")) == str(product_id)]
        if not filtered_data:
            return {"error": f"Aucun produit trouvé avec l'id {product_id}."}, 404
        return {"products": filtered_data}
    return {"products": data}

def products_csv():
    with open('products.json') as f:
        data = json.load(f)
    product_id = request.args.get('id')
    if product_id is not None:
        filtered_data = [item for item in data if str(item.get("id")) == str(product_id)]
        if not filtered_data:
            return {"error": f"Aucun produit trouvé avec l'id {product_id}."}, 404
        return {"products": filtered_data}
    return {"products": data}
