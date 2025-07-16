import json
from flask import Flask, render_template

app = Flask(__name__)

with open('items.json') as f:
    data = json.load(f)
    items = data.get('items', [])

@app.route('/items')
def contact():
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)