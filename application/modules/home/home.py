from flask import Blueprint, render_template, request, redirect, url_for
from application.models.models import db, Veevainfo

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@home_bp.route('/')
def home():
    veeva_users = Veevainfo.query.all()
    return render_template("home.html", veeva_users = veeva_users)
