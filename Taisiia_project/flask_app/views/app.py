from flask import Blueprint, render_template, request, abort, redirect, Flask
from flask_paginate import get_page_parameter, Pagination
from sqlalchemy import select
from forms import ShoppingForm
from flask_wtf.csrf import CSRFProtect
import secrets


shopping_bp = Blueprint("shopping_bp", __name__, url_prefix="/shopping-list")
#shopping_bp = Flask(__name__)

CSRFProtect(shopping_bp)
shopping_bp.config['SECRET_KEY'] = secrets.token_hex(16)
shopping_bp.jinja_env.add_extension("jinja2.ext-do")


@shopping_bp.route("/")
def home():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    page_size = 10

    query = select(ShoppingForm).order_by(ShoppingForm.product)
    pagination = shopping_bp.paginate(query, page=page, per_page=page_size)

    return render_template(
        "shopping_list.html",
        shopping_list=pagination.items,
        pagination=Pagination(
            page=page,
            per_page=page_size,
            total=pagination.total,
            css_framework="bootstrap5",
            record_name="shopping_list",
        ),
    )

@shopping_bp.route("/base")
def base():
    return render_template("base.html")

shopping_list = [
    {"id": 1, "product": "Sneakers", "brand": "Adidas", "color": "black"},
    {"id": 2, "product": "Jeans", "brand": "Levi's", "color": "blue"},
    {"id": 3, "product": "Loafers", "brand": "Reformation", "color": "black"},
    {"id": 4, "product": "Dress", "brand": "Zara", "color": "black"},
    {"id": 5, "product": "Long-Sleeve", "brand": "Everlane", "color": "gray"},
]

@shopping_bp.route("/products")
def list_items():
    return render_template("shopping/list.html", shopping_list=shopping_list)

@shopping_bp.route("/product/<int:product_id>")
def item_details(product_id):
     product = get_item_by_id(product_id)
     return render_template("shopping/list.html", shopping_list=[product])

@shopping_bp.route("/product/add", methods=["GET", "POST"])
def create_product():
    shopping_form = ShoppingForm()
    if request.method == "POST" and shopping_form.validate_on_submit():
        product = shopping_form.product.data
        brand = shopping_form.brand.data
        color = shopping_form.color.data
        shopping_list.append({"id": len(shopping_list) + 1, "product": product, "brand": brand, "color": color})
        return redirect("/shopping-list")
    return render_template("shopping/add", shopping_form=shopping_form)

@shopping_bp.route("/product/<int:product_id>/edit", methods=["GET", "POST"])
def edit_product(product_id):
    product = get_item_by_id(product_id)
    shopping_form = ShoppingForm(data=product)
    if request.method == "POST" and shopping_form.validate_on_submit():
        product["product"] = shopping_form.product.data
        product["brand"] = shopping_form.brand.data
        product["color"] = shopping_form.color.data
        return redirect("/shopping-list")
    return render_template("shopping/edit.html", shopping_form=shopping_form)

@shopping_bp.route("/product/<int:product_id>/delete", methods=["GET", "POST"])
def delete_product(product_id):
    product = get_item_by_id(product_id)
    shopping_list.remove(product)
    return redirect("/shopping-list")


def get_item_by_id(product_id):
    for product in shopping_list:
        if product["id"] == product_id:
            return product
    abort(404)

def add_product():
    return render_template("shopping/add.html")

#if __name__=="__main__":
#   shopping_bp.run(debug=True)