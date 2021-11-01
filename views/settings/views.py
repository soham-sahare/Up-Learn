from utils import *

settings_ = Blueprint('settings', __name__)

@settings_.route("/settings", methods = ["GET", "POST"])
@login_required
def settings():
    data = {
        "username": session["username"]
    }
    return render_template("/settings/settings.html", data=data)

@settings_.route("/settings/account-information", methods = ["GET", "POST"])
@login_required
def account_information():
    user = UserModel.query.filter_by(id = session["id"]).first()
    if request.method == "POST":    
        if request.form["phone"] != "":
            if not request.form["phone"].isnumeric():
                flash("Phone Number should be only numeric.")
                return redirect("/settings/account-information")

            if len(request.form["phone"]) != 10:
                flash("Phone Number should be of 10 characters.")
                return redirect("/settings/account-information")
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.phone = request.form["phone"]
        user.about_me = request.form["about_me"]
        user.title = request.form["title"]
        db.session.commit()
        flash("Data Saved.")
        return redirect("/settings/account-information")
    data = {
        "user": user
    }
    return render_template("/settings/account-information.html", data=data)

@settings_.route("/settings/social-network", methods = ["GET", "POST"])
@login_required
def social_network():
    user = UserModel.query.filter_by(id = session["id"]).first()
    if request.method == "POST":
        user.facebook = request.form["facebook"]
        user.linkedin = request.form["linkedin"]
        user.github = request.form["github"]
        user.instagram = request.form["instagram"]
        db.session.commit()
        flash("Data Saved.")
        return redirect("/settings/social-network")
    data = {
        "user": user
    }
    return render_template("/settings/social-network.html", data=data)

@settings_.route("/settings/change-password", methods = ["GET", "POST"])
@login_required
def change_password():
    user = UserModel.query.filter_by(id = session["id"]).first()
    if request.method == "POST":
        current_password = request.form["current_password"]
        new_password = request.form["new_password"]
        new_confirm_password = request.form["new_confirm_password"]
        if user.check_password(current_password):
            if len(new_password) < 7:
                flash("Password should be greater than 6 characters.")
                return redirect("/settings/change-password")
            if new_password != new_confirm_password:
                flash("Passwords did'nt matched.")
                return redirect("/settings/change-password")
            user.set_password(new_password)
            db.session.add(user)
            db.session.commit()
            flash("Password reset successful. Now login.")
            return redirect("/authentication/logout")
        else:
            flash("Current Password incorrect. Please try again.")
            return redirect("/settings/change-password")
    data = {
        "user": user
    }
    return render_template("/settings/change-password.html", data=data)