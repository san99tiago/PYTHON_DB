# BASIC OOP TO APPROACH DATABASES IN PYTHON
# Santiago Garcia Arango, August 2020

class Person:
    def __init__(self, name, last, sex, age):
        self.name = name
        self.last = last
        self.sex = sex
        self.age = age
        self.create_mail()

    def create_mail(self):
        # First would be important to check that it doesn't exist...
        self.mail = self.name + "." + self.name + "@santi.com"

    def get_full_name(self):
        return(self.name + " " + self.last)

    def get_mail(self):
        return(self.mail)

    def is_adult(self):
        if self.age > 20:
            return(True)
        else:
            return(False)


# We create simple basic "test" of the created class
P1 = Person("Santiago", "Garcia", "Male", 20)
print("NAME = ", P1.get_full_name())
print("MAIL = ", P1.get_mail())
print("ADULT = ", P1.is_adult())
