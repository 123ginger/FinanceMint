from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

app.secret_key = "vra8eppuJ9vOYP/ybw=="


@app.route("/")
def home1():
    return render_template("login.html")

# homepage
@app.route("/home")
def home():
    return render_template("homepage.html")
    # Do I need this in all my functions to make sure people are logged in before entering website?
    #if "username" in session:
        #return render_template("homepage.html")
    #else:
        #return redirect(url_for('login'))


# login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        # check if there is a person like this
        user = db_session.query(User).where((User.username == username) & (User.password == password)).first()
        if user == None:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))



# signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # ask for new username and password, check if unique, then add to database and redirect to new page
    if request.method=="GET":
        return render_template("signup.html")
    elif request.method == "POST":
        # ask for content
        username = request.form["username"]
        password = request.form["password"]
        password_check = request.form["password-check"]
        # check that there are no passwords like that and it matches the check 
        user = db_session.query(User).where((User.username == username)).first()
        if (user is None) and (password == password_check):
            temp = User(username, password)
            db_session.add(temp)
            db_session.commit()
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return redirect(url_for("signup"))
            
        
          
# Forum page
@app.route("/forum", methods=["GET", "POST"])
def forum():
    if request.method=="GET":
        return render_template("forum.html")
    elif request.method == "POST":
        content = request.form["post-text-area"]
        date = request.form["post-date-input"]
        type = request.form["post-type-select"]
        sort_by = request.form["post-sort-by"]
        temp = Post(content, date, type)
        db_session.add(temp)
        db_session.commit()
        # print the posts being made while on page
        records = db_session.query(Post).all()
        return render_template('forum.html', records=records)
    
        # sort the posts 
        #sorted_posts = db_session.query(Post).where((sort_by == Post.type)).first()
        #posts = db_session.query(Post)
        #if sorted_posts == None:
            # how to do actual print for posts
            #print(posts)
        #else:
            #print(sorted_posts)


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
