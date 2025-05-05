class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Makes a generic animal sound.")
        
    def describe(self):
        print(f"{self.name} is {self.age} years old.")