# Lists
list_new = []

list_new.append("1")
list_new.append("2")
list_new.insert(0,"0")
list_new.remove("0")
list_new.pop(0) # pops the given index
# list_new.clear()
print("list_new Count: ", list_new.count("2")) # Return the number of times x appears in the list_new.
list_new.reverse()

# Using list_news as Stacks
# Stack: Last in first out
# Python's pop() and append() methods allow us to use list_news as stacks.

# Using list_news as Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft() # Removes the first item.
print("Queue:", queue)

# Python Map Function
# Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, list_news, etc.). It is used when you want to apply a single transformation function to all the iterable elements.

"""
Syntax: 
map(fun, iter)
-> fun: It is a function to which map passes each element of given iterable.
-> iter: It is a iterable which is to be mapped.
"""

squares = list(map(lambda x: x**2, range(10)))
squares_other = [x**2 for x in range(10)]
interesting = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print("Squares List:", squares)
print("interesting list:",interesting)

# Del Function
# del() => The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a # removes all the variables from the list.

# Tuples
t = 12345, 54321, 'hello!'
x,y,z = t

# Note: Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print("u tuple:", u)
# Tuples are immutable: # cannot assign item later
# for example, "t[0] = 88888" command will throw error.

print("u length:", len(u))

# Sets: A set is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket set:",basket) # show that duplicates have been removed
a = set('abracadabra') # unique letters in a
print("a set:", a)

# Dictionaries
tel = {'jack': 4098, 'sape':4139}
tel["guido"] = 4127
print("jack tel:", tel['jack'])

del tel['sape'] # deleting a dict element
print("tel keys:", tel.keys())
print("tel values:", tel.values())
print("tel items:", tel.items())
car = {'model': "BMW", "door_count": '5'}
for k,v in car.items():
    print("key:", k, " value:",v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(q, ":", a)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


