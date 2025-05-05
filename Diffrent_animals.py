from animal import Animal

class Lion(Animal):    
    def make_sound(self):
        print("Roar!")
    def roar(self):
        print("Roars loudly.")

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")
    def fly(self):
        print("Flies high in the sky.")

class Reptile(Animal):
    def make_sound(self):
        print("Hiss!")
    def crawl(self):
        print("Crawls stealthily.")