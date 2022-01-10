
class Movies:
   def __init__(self, title, year, genre):
       self.title = title
       self.year = year
       self.genre = genre
       #Variables
       self._views = 0

   def __str__(self):
       return f"{self.title} ({self.year})"

   def play(self, step=1):
       self.views += step
    
   @property      #zamiana metody w argument
   def views(self):
       return self._views
   @views.setter
   def views(self, value):
       self._views = value


class Series:
   def __init__(self, title, year, genre, episode, season):
       self.title = title
       self.year = year
       self.genre = genre
       self.episode = episode
       self.season = season
       #Variables
       self._views = 0

   def __str__(self):
       return f"{self.title} S{self.season}E{self.episode}"
   
   def play(self, step=1):
       self.views += step

   @property      #zamiana metody w argument
   def views(self):
       return self._views
   @views.setter
   def views(self, value):
       self._views = value


bluesbrothers = Movies(title="The Blues Brothers", year="1980", genre="Road Movie")
greenbook = Movies(title="The Green Book", year="2020", genre="Road Movie") 
diune = Movies(title="Diune", year="2021", genre="Science Fiction") 
diehard = Movies(title="The Die Hard", year="1994", genre="Action")  
simpsons11 = Series(title="The Simpsons", year="1997", genre="Animated", episode="01", season="01")
simpsons12 = Series(title="The Simpsons", year="1997", genre="Animated", episode="02", season="01")
simpsons13 = Series(title="The Simpsons", year="1997", genre="Animated", episode="03", season="01")
simpsons14 = Series(title="The Simpsons", year="1997", genre="Animated", episode="04", season="01")
simpsons21 = Series(title="The Simpsons", year="1998", genre="Animated", episode="01", season="02")
simpsons22 = Series(title="The Simpsons", year="1998", genre="Animated", episode="02", season="02")
simpsons23 = Series(title="The Simpsons", year="1998", genre="Animated", episode="03", season="02")
simpsons24 = Series(title="The Simpsons", year="1998", genre="Animated", episode="04", season="02")

library = [bluesbrothers, greenbook, diune, diehard, simpsons11, simpsons12, simpsons13, simpsons14, simpsons21, simpsons22, simpsons23, simpsons24]

def get_movies():
    for n in library:
        if isinstance(n, Movies):
            print(n)


def get_series():
    for n in library:
        if isinstance(n, Series):
            print(n) 


def search(q):
    for a in library:
        if q == a.title:
            print(a)
if __name__ == "__main__":
    q = input("Podaj proszę szukany tytuł: ")
    search(q)


import random
def generate_views():
    r = random.choice(library)
    r.views =+ random.choice(range(1,101))
    print(f"{r} views: {r.views}")
     

def ten_generate_views():
    for i in range(10):
        generate_views()

top_titles_dict = {}
def top_titles():
    for a in library:
        top_titles_dict[f"{a}"] = [a.views]
    top_titles_list = sorted(top_titles_dict.items(), key = lambda x: x[1], reverse=True)
    return print(top_titles_list[0:l])
if __name__ == "__main__":
    l = int(input("Podaj proszę wybraną ilość najpopularniejszych tytułów: "))
    top_titles()



print("Biblioteka filmów")
get_movies()
get_series()
ten_generate_views()
import time
print("Najpopularniejsze filmy i seriale dnia",time.strftime("%d:%m:%Y", time.localtime()))
top_titles()