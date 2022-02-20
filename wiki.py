"""This function works with the wiki api, creates and returns a url"""

import requests

def url_api(movie_name):
    """
    Function receives name of movie that we want url for. Then makes API call
    to receieve id of the wiki page of that specific movie. Returns url to homepage
    function.
    """
    session_name = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    search_page = movie_name

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_page
    }
    response = session_name.get(url=url, params=params)
    data = response.json()
    page_id = data['query']['search'][0]['pageid']
    url_page = "http://en.wikipedia.org/?curid=" + str(page_id)
    return url_page
