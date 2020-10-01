
import requests
import pprint

# Grab data from themoviedb.org using their API v3
# API removed from files
# API key removed

api_key = "e221e60130b417cf3783e7f7c5c029a2"

url_example = "https://api.themoviedb.org/3/movie/550?api_key=e221e60130b417cf3783e7f7c5c029a2"
base_url = "https://api.themoviedb.org/"
api_version = 3
# api path to search movie using movie ID
movie_id = 100
api_path = "/search/movie"
movie_name = "The Hangover"
endpoint = f"{base_url}{api_version}{api_path}?api_key={api_key}&query={movie_name}"

# request api information
r = requests.get(endpoint)
data = r.json()
# print(data)
results = data['results']
for movie in results:
    _id = movie['id']
    title = movie['title']
    print(_id, title)