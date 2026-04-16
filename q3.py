class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat names {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()
class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says woof!")
    def __str__(self):
        return f"<A dog named {self.name}>"
boba = Dog("Boba")
boba.speak()
print(boba)
