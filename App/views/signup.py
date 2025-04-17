
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required
)

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')


@signup_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')
