"""
Sınıflarda özitelik ve örnekleri
"""

class Person:
    def __init__(self, name, profession, age):
        self.name = name
        self.profession = profession
        self.age = age
        
    def disp(self):
        print(self.name, self.profession, self.age)
        
per = Person("Fatih NALBANT", "Mühendis", "32")
per.disp()
