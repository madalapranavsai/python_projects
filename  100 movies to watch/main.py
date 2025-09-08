import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response=requests.get(URL)
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")

all_movies=soup.find_all("h3",class_="title")
movie_titles=[movie.get_text() for movie in all_movies]
movies=movie_titles[::-1]

with open("movies.txt","w") as file:
    for movie in movies:
        file.write(movie+"\n")

