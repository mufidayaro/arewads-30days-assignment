#Exercise 1

#Python --version
#Exercise 2
a = 3
b = 4
print( a + b)
print( a - b)
print( a * b)
print( a % b)
print( a / b)
print( a ** b)
print( a // b)

#Exercise 3
a = "My name is Mufida"
b = "My family name is Garba Yaro"
c = "The name of my country is Nigeria"
d = "I am enjoying 30 days of python"
print(a)
print(b)
print(c)
print(d)

#Exercise 4
a = [10,9.8,3.14,4-4j,['Asabeneh', 'Python', 'Finland'],'Mufida','garba yaro','Nigeria']
for i in a:
    print(type(i))
    
#Level 3 Exercise1

# Integer data type
a = 10  
print(a)
# Float data type
b = 3.14
print(b)
# Complex data type
c = 1 + 2j
print(c)
# String data type
name = "Mufida"  
print(name)
# Boolean data type
is_agirl = True  
print(is_agirl)
# List data type
numbers = [1, 2, 3, 4, 5]  
print(numbers)
# Tuple data type
vegetables = ("carrot", "cucumber", "lettuce")  
print(vegetables)
# Set data type
fruits = {"mango", "grape", "guava"}  
print(fruits)
# Dictionary data type
person = {'name': 'Mufida', 'age': 21, 'country': 'Nigeria'}  
print(person)
    
# level 3 Exercise 2
import math

def euclidean_distance(a1, b1, a2, b2):
  distance = math.sqrt(((a2 - a1) ** 2) + ((b2 - b1) ** 2))
  return distance

a1 = 2
b1 = 3
a2 = 10
b2 = 8

distance = euclidean_distance(a1, b1, a2, b2)
print(distance)    