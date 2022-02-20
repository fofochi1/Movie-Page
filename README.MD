# Name
The Movie App

## Description
This app gathers information about a movie that is randomly chosen from a list. It uses a couple of APIs where the information is stored.

### Technologies
This app uses Flask, Html, CSS and Jinja

### Libraries
random, os, requests, dotenv, flask

### APIs
TMDB (The Movie Database)
Wikipedia api

#### Instructions
You will need to get an API key for TMDB. Place that key inside a .env file so that it is hidden from anyone else.
Installations needed are Flask, requests and dotenv.

#### Heroku Link
mighty-lowlands-93826.herokuapp.com

#### Questions

1)What are at least 3 technical issues you encountered with your project? How did you fix them?
a)One of the issues I arrived at was with the Wikipedia api call. It was a little confusing as to what I needed to retrieve in order to get the url for. I solved it by looking at the documentation and seeing that each wiki page has a specific ID, then that is what I am receiving from that api call to create the url.
b)Another technical issue I was having was with the response of the TMDB api call. I kept trying to parse through it but it was just very hard to look at. I was able to solve what to get and how to get by using the documentation of TMDB. It shows it very well in the website, as to in what order everything is.
c)The third issue I was having was with receiving the image of the movie. Linking to the image tag on the html was a little confusing and was just much bigger than I wanted. I was able to size it down with CSS. I was also able to link to the image tag by looking at how Jinja uses variables in Html.

2)What are known problems (still existing), if any, with your project? 
A problem that still exists in my project is the fact that sometimes using the randomizer to pick the movie in the list, the randomizer will sometimes pick the same movie.

3)What would you do to improve your project in the future? 
What I would like to improve is how the app looks in the website. I feel like it is a little basic, so I think I can do better with that and how it is displayed.

# Alfonso Buzeta Borquez
## SWE Section 002