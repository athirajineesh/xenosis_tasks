class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_specs(self):
        print("Name:", self.name)
        print("Age:", self.age)


person1= Person("Athira","28")
person2= Person("Jineesh","35")
person3= Person("Anoop","25")
person4= Person("Dhaniji","28")

print("\nPerson Details:")
person1.display_specs()
person2.display_specs()
person3.display_specs()
person4.display_specs()



