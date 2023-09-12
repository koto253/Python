
class Person:
    def __initi__(self, name, dob, hair_color, nationality):
        self.name = name
        self.dob = dob
        self.hair_color = hair_color
        self.nationality = nationality

    def printIdentity(self):
        print("Im " + self.name + "I am born in " + str(self.dob) + " and my nationality is " + self.nationality)

identity = Person("Ismael", 1995, "black", "Guinean")
identity.printIdentity()
