import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movie_title = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_title = [movie.getText() for movie in all_movie_title]
movies = movie_title[::-1]

with open("movies1.txt", mode="w",encoding="utf-8") as file:
    for n in movies:
        file.write(f"{movies}\n")





'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''