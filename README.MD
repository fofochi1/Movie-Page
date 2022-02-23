# Name
The Movie App

## Description
This app gathers information about a movie that is randomly chosen from a list. It uses a couple of APIs where the information is stored.
There is user created accounts that can leave reviews for the movie.

### Technologies
This app uses Flask, Html, CSS and Jinja, SQLalchemy

### Libraries
random, os, requests, dotenv, flask, flask_sqlalchemy, flask_login

### APIs
TMDB (The Movie Database)
Wikipedia api

#### Instructions
You will need to get an API key for TMDB. Place that key inside a .env file so that it is hidden from anyone else.
Installations needed are Flask, requests, dotenv and sqlalchemy.
Place DATABASE_URL inside .env file.
Place a created SECRET_KEY inside .env file.

#### Heroku Link
https://sheltered-ravine-80246.herokuapp.com

#### Questions

1)What are at least 2 technical issues you encountered with your project? How did you fix them? 
One of the problems I ran in to is creating the user account with a password. I was able to solve it by looking at flask-login documentation
and reading up on how to verify the login after the form.
The second problem I ran in to is when leaving a review, I needed to figure out how to get it connect to the database for just that one movie. I was able to solve this by creating an extra text input that automatically filled it up with the movie name and the user name so that the movie name, username, review number and review would all go to the database.

2)How did your experience working on this milestone differ from what you pictured while working through the planning process? What was unexpectedly hard? Was anything unexpectedly easy?
I thought this milestone was a bit harder than the first one. The reason I thought it was harder is because of the database and dealing with querying to it. During the planning, I was able to think of the logic to create the user and login, but then I had to figure out how to connect the movie review to the database. The unexpected part that was hard was the part of having the user stay logged in after creating a review, at first it would always logout right after submitting a review, but then using flask-login manager, I was able to figure it out.

# Alfonso Buzeta Borquez
## SWE Section 002