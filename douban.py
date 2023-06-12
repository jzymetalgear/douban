import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_movies():
    url = "https://www.imdb.com/chart/top"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_list = soup.select("tbody.lister-list tr")

    top_movies = []
    for movie in movie_list:
        rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
        title = movie.find("td", class_="titleColumn").a.text
        rating = movie.find("td", class_="ratingColumn").strong.text
        top_movies.append({"Rank": rank, "Title": title, "Rating": rating})

    return top_movies

top_movies = get_top_movies()
df = pd.DataFrame(top_movies)
df.to_excel("top_movies.xlsx", index=False)
