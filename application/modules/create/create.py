from flask import Blueprint, render_template, request, redirect, url_for
from application.models.models import db, Veevainfo

create_bp = Blueprint('create_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@create_bp.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        veeva_user = Veevainfo(
            rtsm_url=request.form["rtsm_url"],
            username=request.form["username"],
            password=request.form["password"]
        )
        db.session.add(veeva_user)
        db.session.commit()
        veeva_users = Veevainfo.query.all()
        return redirect(url_for("home_bp.home", veeva_users = veeva_users))
   
    return render_template("create.html")
