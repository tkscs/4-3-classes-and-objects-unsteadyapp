class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says woof!")

boba = Dog("Boba")
boba.speak()
