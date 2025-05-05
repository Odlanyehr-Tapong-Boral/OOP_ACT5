from Diffrent_animals import Lion
from Diffrent_animals import Bird
from Diffrent_animals import Reptile

def test_animals():
    lion = Lion("Lionel", 24)
    bird = Bird("Birb", 5000)
    reptile = Reptile("SolidSnake", 23)

    lion.describe()
    lion.make_sound()
    lion.roar()
    print()

    bird.describe()
    bird.make_sound()
    bird.fly()
    print()

    reptile.describe()
    reptile.make_sound()
    reptile.crawl()

if __name__ == "__main__":
    test_animals()
