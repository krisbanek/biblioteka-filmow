class Movies:
   def __init__(self, title, year, genre):
       self.title = title
       self.year = year
       self.genre = genre
       #Variables
       self.views = 0

   def __str__(self):
       return f"{self.title} ({self.year})"

   def play(self, step=1):
       self.views += step

class Series:
   def __init__(self, title, year, genre, episode, season):
       self.title = title
       self.year = year
       self.genre = genre
       self.episode = episode
       self.season = season
       #Variables
       self.views = 0

   def __str__(self):
       return f"{self.title} S{self.season}E{self.episode}"
   
   def play(self, step=1):
       self.views += step

bluesbrothers = Movies(title="The Blues Brothers", year="1980", genre="Road Movie") 
simpsons = Series(title="The Simpsons", year="1997", genre="Animated", episode="01", season="05")

print(simpsons)
print(bluesbrothers)

print(simpsons.views)
simpsons.play()
print(simpsons.views)
