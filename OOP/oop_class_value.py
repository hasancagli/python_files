# CLASS VALUE
class Person:
    # Those values are immutable and constant variables of a class.
    number_of_people = 0
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name 
        Person.number_of_people += 1
    
p1 = Person("tim")
p2 = Person("tim2")

print(Person.number_of_people)

# CLASS METHOD

class People:
    # Those values are immutable and constant variables of a class.
    number_of_people = 0
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name 
        People.add_person()
        
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
        
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
s1 = People("tim")
s2 = People("tim2")

print(People.number_of_people_())

# STATIC METHOD
class Math_Class:
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10

print(Math_Class.add5(5))







