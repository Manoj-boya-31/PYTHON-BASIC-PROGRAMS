class Movie:
    def __init__(self,film,hero,year,status):
        self.film=film
        self.hero=hero
        self.year=year
        self.status=status
    def ran(self):
        print("This movie was running in theatres")
    def ott(self):
        print("This movie is now in OTT")