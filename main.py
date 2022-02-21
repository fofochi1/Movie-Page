"""
Main page of the application. Sends information to wiki.py, tmdb.py and index.html
"""

from random import randrange
import os
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from dotenv import find_dotenv, load_dotenv
from wiki import url_api
from tmdb import api_call
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user




load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = "I am a secret"

# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(50))
    user = db.Column(db.String(120))
    review = db.Column(db.String(200),nullable=False)
    stars = db.Column(db.String(2),nullable=False)

    def __init__(self, movie, user, review, stars):
        self.movie = movie
        self.user = user
        self.review = review
        self.stars = stars


db.create_all()

BASE_URL = "https://api.themoviedb.org/3/movie/"
movies = ["155","49521","791373", "634649", "370172", "460465", "27205","11688", "864", "207703"]


@app.route("/homepage", methods=['POST', 'GET'])
@login_required
def homepage():
    """
    This is the main function. It does the API call to TMDB. Calls functions api_call
    which handles the results of TMDB call. Then calls url_api function to get the
    Wiki url of the movie. Will then send info to html using render_template.
    """
    if(current_user.username):
        random_number = randrange(len(movies))
        response = requests.get(BASE_URL + movies[random_number] + "?api_key=" + os.getenv("TMDB_KEY"))
        array = response.json()
        movie_details = api_call(array)
        page_url = url_api(movie_details["Name"])
        movie_review = Message.query.filter_by(movie=movie_details['Name']).limit(5).all()
        return render_template("index.html", movie_details = movie_details, page_url = page_url, movie_review=movie_review, current_user=current_user.username)
    else:
        return redirect("login_screen")

@app.route('/reviews_form', methods=['POST'])
def reviews_form():
    movie = request.form.get('movie')
    user = request.form.get('user')
    review = request.form.get('review')
    stars = request.form.get('stars')
    review_to_send = Message(review=review, stars=stars, movie=movie, user=user)
    review_to_send = Message(review=review, stars=stars, movie=movie, user=user)
    db.session.add(review_to_send)
    db.session.commit()
    return redirect(url_for("homepage"))
    


@app.route('/login_form', methods=['POST'])
def login_post():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not user.password == password:
        flash('Please check your login details and try again.')
        return redirect(url_for('login_screen')) # if the user doesn't exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the right credentials
    #return homepage(username)
    else:
        login_user(user, remember=True)
        return redirect(url_for('homepage'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/signup', methods=['POST'])
def signup():
    # code to validate and add user to database goes here
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Username already exists')
        return redirect(url_for("signup_screen"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=username, password=password)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login_screen'))

@app.route("/")
def login_screen():
    return render_template('login.html')

@app.route("/signup_screen")
def signup_screen():
    return render_template('register.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_screen'))




app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
