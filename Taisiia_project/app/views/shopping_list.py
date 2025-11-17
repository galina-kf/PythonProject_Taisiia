from flask import Blueprint
from flask import render_template, request, abort, redirect
from Taisiia_project.app.forms import ShoppingForm
from Taisiia_project.app.models import Product



shopping_bp = Blueprint('shopping_list', __name__, url_prefix='/shopping_list')

shopping_list = [
    {"id": 1, "product": "Sneakers", "brand": "Adidas", "color": "black"},
    {"id": 2, "product": "Jeans", "brand": "Levi's", "color": "blue"},
    {"id": 3, "product": "Loafers", "brand": "Reformation", "color": "black"},
    {"id": 4, "product": "Dress", "brand": "Zara", "color": "black"},
    {"id": 5, "product": "Long-Sleeve", "brand": "Everlane", "color": "gray"},
]

@shopping_bp.route("/")
def list_items():
    return render_template("shopping/list.html", shopping_list=shopping_list)

@shopping_bp.route("/<int:product_id>/")
def product_details(product_id):
     product = get_item_by_id(product_id)
     return render_template("shopping/list.html", shopping_list=[product])

@shopping_bp.route("/add/", methods=["GET", "POST"])
def create_product():
    shopping_form = ShoppingForm()
    if request.method == "POST" and shopping_form.validate_on_submit():
        product = shopping_form.product.data
        brand = shopping_form.brand.data
        color = shopping_form.color.data
        description = shopping_form.description.data
        shopping_list.append({"id": len(shopping_list) + 1, "product": product, "brand": brand, "color": color, "description": description})
        return redirect("/shopping-list")
    return render_template("shopping/add", shopping_form=shopping_form)

@shopping_bp.route("/<int:product_id>/edit/", methods=["GET", "POST"])
def edit_product(product_id):
    product = get_item_by_id(product_id)
    shopping_form = ShoppingForm(data=product)
    if request.method == "POST" and shopping_form.validate_on_submit():
        product["product"] = shopping_form.product.data
        product["brand"] = shopping_form.brand.data
        product["color"] = shopping_form.color.data
        product["description"] = shopping_form.description.data
        return redirect("/shopping-list")
    return render_template("shopping/edit.html", shopping_form=shopping_form)

@shopping_bp.route("/<int:product_id>/delete/", methods=["GET", "POST"])
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
