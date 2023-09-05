from flask import Flask, jsonify, request

products = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"}
]

app = Flask(__name__)

# curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(products)


# curl -v http://localhost:5000/product/1
@app.route("/product/<int:id>")
def get_product(id):
    product_list = [product for product in products if product["id"] == id]
    if len(product_list) == 0:
        return f"Product with id {id} not found", 404
    return jsonify(product_list[0])

@app.route("/product", methods=["POST"])
def post_product