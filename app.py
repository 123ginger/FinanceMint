"""
A fully functioning website that is aimed to address the economic difficulties 
that come with living in the bay area.

Created by: Bradford Tudor 
Date: May 2023
"""

from flask import *
from database import init_db, db_session
from models import *
from datetime import datetime

app = Flask(__name__)

app.secret_key = "vra8eppuJ9vOYP/ybw=="


# homepage functionality
@app.route("/home")
def home():
    # If someone is logged in then they can go to the page when submitting the website url 
    # if they are not then they will be directed to the login page
    if "username" in session:
        return render_template("homepage.html")
    else:
        return redirect(url_for("login"))


# login functionality
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    # gets the inputted values from the form and establishes the current user
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        # check if there is already a user with same credentials 
        user = db_session.query(User).where((User.username == username) & (User.password == password)).first()
        if user == None:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))


# signup functionality
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    elif request.method == "POST":
        # retrieving input from signup form
        username = request.form["username"]
        password = request.form["password"]
        password_check = request.form["password-check"]
        # check that information is unique and that there is no user with that same username
        user = db_session.query(User).where((User.username == username)).first()
        if (user is None) and (password == password_check):
            # create new user object, add to database, and set a new current user
            temp = User(username, password)
            db_session.add(temp)
            db_session.commit()
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return redirect(url_for("signup"))      


# Forum functionality
@app.route("/forum", methods=["GET", "POST"])
def forum():
    # user cannot get to these pages unless they are signed in
    if "username" in session:
        if request.method=="GET":
            return render_template("forum.html")
        elif request.method == "POST":
            # retrieves input from form on forum page
            content = request.form["post-text-area"]
            date = datetime.now().date()
            type = request.form["post-type-select"]
            sort_by = request.form["post-sort-by"]
            # creates a new post and adds to database
            temp = Post(content, date, type, session["username"])
            db_session.add(temp)
            db_session.commit()
            # prints the posts on the page by the special case sorting mechanisms (all, user-contributions, today-posted)
            if sort_by == "all":
                records = db_session.query(Post).all()
                return render_template('forum.html', records=records)
            elif sort_by == "user_contributions":
                records = db_session.query(Post).where(Post.user_id == session["username"])
                return render_template('forum.html', records=records)
            elif sort_by == "today-posted":
                records = db_session.query(Post).where(Post.date == datetime.now().date())
                return render_template('forum.html', records=records)
            else:
                # if not one of these specific cases then sort normally by comparing the type to our databases type
                records = db_session.query(Post).where((Post.type == sort_by)).all()
                return render_template('forum.html', records = records)
    else:
        return redirect(url_for("login"))


# logout functionality
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("login"))
 

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5002)
