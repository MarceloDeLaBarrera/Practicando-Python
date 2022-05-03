import requests

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMmQxYWJlNmQ4NDM0ZjRkNGY4ZDU4Y2I4MWE5MTRlMCIsInN1YiI6IjYxN2E0MDlhMjI5YWUyMDA0NGM2YmViMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2cNe0PX1Snx_qARyaTfxbSxynT3y-m8E7Bi0rf4aS9I"
baseurl = "https://api.themoviedb.org/3/"
movie_id = 100
URI = "search/movie"
endpoint = baseurl+URI
headers = {"Authorization": f"Bearer {token}"}
params = {"query": "avengers"}
response = requests.get(endpoint, headers=headers, params=params)
print(response.url)
print(response.headers)
data = response.json()
# print(data)
for movie in data["results"]:
    if movie["vote_average"] > 8:
        print(movie["title"])

vote_average = set()
for movie in data["results"]:
    vote_average.add(movie["vote_average"])

distinct_votes = list(vote_average)
distinct = len(distinct_votes)
totalresults = (data["total_results"])
print(f"{totalresults-distinct} movies has the same vote")
