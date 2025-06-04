from flask import render_template, redirect, url_for, request
from app import app
from app.models.product import Product
from app.forms import ProductForm
import os
import json

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract")
def display_form():
    form = ProductForm()
    return render_template("extract.html", form=form)

@app.route("/extract", methods=['POST'])
def extract():
    form = ProductForm(request.form)
    if form.validate():
        product_id = form.product_id.data
        product = Product(product_id)
        if_not_exists = product.if_not_exists()
        if if_not_exists:
            form.product_id.errors.append(if_not_exists)
            return render_template("extract.html", form=form)
        product.extract_reviews().extract_name().calculate_stats()
        product.export_reviews()
        product.export_info()
        return redirect(url_for('product', product_id=product_id))
    else:
        return render_template("extract.html", form=form)

@app.route("/products")
def products():
    products_files = os.listdir("app/data/products")
    products = []
    for filename in products_files:
        with open(f"./app/data/products/{filename}", "r", encoding="utf-8") as jf:
            product = Product(filename.split(".")[0])
            product.info_from_dict(json.load(jf))
            products.append(product)
    return render_template("products.html", products=products)

@app.route("/product/<product_id>")
def product(product_id):
    return render_template("product.html", product_id=product_id)

@app.route("/charts/<product_id>")
def charts(product_id):
    return render_template("charts.html", product_id=product_id)

@app.route("/author")
def author():
    return render_template("author.html")