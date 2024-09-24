from flask import Blueprint


vuhitra_ext = Blueprint(
    "vuhitra_ext", __name__)


def page():
    return "Hello, vuhitra_ext!"


vuhitra_ext.add_url_rule(
    "/vuhitra_ext/page", view_func=page)


def get_blueprints():
    return [vuhitra_ext]
