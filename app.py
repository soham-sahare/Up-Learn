from utils import *

###################### Import Blueprints ######################
from views.projects.views import projects_
from views.authentication.views import authentication
from views.settings.views import settings_
###############################################################

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PERMANENT_SESSION_LIFETIME"] =  timedelta(minutes=10)
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

global COOKIE_TIME_OUT
COOKIE_TIME_OUT = 60*5 

###################### Register Blueprints ######################
app.register_blueprint(projects_)
app.register_blueprint(authentication)
app.register_blueprint(settings_)
#################################################################

db.init_app(app)
login.init_app(app)
login.login_view = "authentication.login"

@app.before_first_request
def create_all():
    db.create_all()

@app.errorhandler(404)
def page_not_found_(e):
    return render_template("error/404.html"), 404

@app.errorhandler(405)
def page_not_foun_(e):
    return render_template("error/404.html"), 405

@app.route("/", methods = ["GET", "POST"])
@login_required
def index():
    data = {
        "username": session["username"]
    }
    return render_template("index.html",  data = data)

@app.route("/user-profile/<id>", methods = ["GET"])
@login_required
def user_profile(id):
    user = UserModel.query.filter_by(name = id).first()
    projects = ProjectsModel.query.filter_by(user_id = session["id"])
    data = {
        "projects": projects,
        "my_id": session["id"],
        "user": user
    }
    return render_template("user-profile.html", data=data)

if __name__ == "__main__":
    app.run(debug = True)