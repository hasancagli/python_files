# Using Inheritance

class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    def speak(self):
        print("Pet speak method")
        
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # Using super() keyword
        self.color = color
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 21, "Red")
c.speak()

d = Dog("Dog", 20)
d.speak()