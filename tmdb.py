"""This function works with the TMDB api, returns a dictionary of information of the movie"""

def api_call(api_response):
    """
    This function receives the results of the TMDB api call and places specific
    elements of that json in variables to then return to homepage function.
    """
    movie_details = {"Name": "", "Overview":"", "Genre":"", "Image":"", "tag":""}
    movie_details.update({"tag": api_response["tagline"]})
    movie_details.update({"Name": api_response["original_title"]})
    movie_details.update({"Overview": api_response["overview"]})
    movie_details.update({"Image": "https://image.tmdb.org/t/p/w500" + api_response["poster_path"]})
    length_of_genre = len(api_response["genres"])
    list_of_genre = []
    for i in range(length_of_genre):
        list_of_genre.append(api_response["genres"][i]["name"])
    new_list_genre = ", ".join(list_of_genre)
    movie_details.update({"Genre": new_list_genre})
    return movie_details
