from datetime import datetime

class Person:
    def __initi__(self, name, dob, hair_color, nationality):
        self.name = name
        self.dob = dob
        self.hair_color = hair_color
        self.nationality = nationality

    def printIdentity(self):
        print(f"I'm {self.name}, I am born in {self.dob}, my nationality is {self.nationality}")

identity = Person("Ismael", 1995, "black", "Guinean")
identity.printIdentity()
