from flask import Blueprint

main = Blueprint('main', __name__)

from main import errors, views, forms

