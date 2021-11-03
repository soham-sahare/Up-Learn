from utils import *

jobsandinternships_ = Blueprint('jobsandinternships', __name__)

@jobsandinternships_.route("/jobs-internships", methods = ["GET", "POST"])
@login_required
def jobsandinternships():
    user = UserModel.query.filter_by(name = session["username"]).first()
    data = {
        "username": session["username"],
        "user": user
    }
    return render_template("jobs-and-internships/jobs_and_internships.html", data=data)

@jobsandinternships_.route("/jobs", methods = ["POST"])
@login_required
def jobs():
    return "Jobs"

@jobsandinternships_.route("/job/<id>", methods = ["GET", "POST"])
@login_required
def job_id(id):
    user = UserModel.query.filter_by(name = session["username"]).first()
    data = {
        "user": user
    }
    return render_template("jobs-and-internships/jobs.html", data=data)

@jobsandinternships_.route("/internships", methods = ["POST"])
@login_required
def internships():
    return "Internships"

@jobsandinternships_.route("/internship/<id>", methods = ["GET", "POST"])
@login_required
def internship_id(id):
    return "Internships {}".format(id)