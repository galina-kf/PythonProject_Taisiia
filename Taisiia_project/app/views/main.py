from flask import render_template, redirect, Blueprint, url_for

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route("/")
def home():
    url_for("shopping.shopping_list")
    return redirect(url_for("shopping.shopping_list"))

@main_bp.route("/base")
def base():
    return render_template("base.html")