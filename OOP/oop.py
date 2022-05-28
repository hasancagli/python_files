class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age 
    
    def add_one(self, x):
        return x+1
    def bark(self):
        print("Bark")
        
d = Dog("Tim", 12)
print(d.get_name())
print(d.get_age())