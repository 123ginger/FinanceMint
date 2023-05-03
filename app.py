from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

app.secret_key = "vra8eppuJ9vOYP/ybw=="


# homepage
@app.route("/")
def home():
    # Do I need this in all my functions to make sure people are logged in before entering website?
    if "username" in session:
        return render_template("homepage.html")
    else:
        return redirect(url_for('login'))


# login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        # check if username and password are correct
        user = db_session.query(User).where((User.username == username) & (User.password == password))
        if user == None:
            flash("Your username/password is incorrect", "error")
            return render_template("login.html")
        else:
            return redirect(url_for("homepage.html"))


# signup
@app.route("/signup")
def signup():
    # ask for new username and password, check if unique, then add to database and redirect to new page
    if request.method=="GET":
        return render_template("login.html")
    elif request.method == "POST":
        # ask for content
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        password_check = request.form["password-check"]
        # check that there are no passwords like that and it matches the check 
        user = db_session.query(User).where((User.username == username) & (User.password == password))
        if (user != None) and (password == password_check):
            temp = User(username, password, email)
            db_session.add(temp)
            db_session.commit()
            return render_template("homepage.html")
        else:
            return render_template("signup.html")
          

# Forum page
@app.route("/forum")
def forum():
    if request.method=="GET":
        return render_template("forum.html")
    elif request.method == "POST":
        content = request.form["post-textarea"]
        date = request.form["post-date-input"]
        type = request.form["post-type-select"]
        word_count = request.form["post-word-count"]
        temp = Post(word_count, content, date, type)
        db_session.add(temp)
        db_session.commit()
        # not the right way to print 
        for posts in Post:
            print(posts)




# How to log out
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged out", "info")
    return redirect(url_for("login"))

            

        
        
         

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)
