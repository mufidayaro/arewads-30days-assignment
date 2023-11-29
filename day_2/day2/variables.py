#Exercise 1: Level 1
# Day 2: 30 Days of python programming
first_name = 'Mufida'
last_name = 'Yaro'
full_name = 'Mufida Garba Yaro'
country = 'Nigeria'
city = 'Kano'
age = 21
year = 2023
is_married = False
is_true = True
is_light_on = True

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Mufida', 'Yaro', 'Mufida Garba Yaro', 'Nigeria', 'Kano', 21, 2023, False, True, True

print(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

#Exercise: level 2
#Exercise 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Exercise 2
print(len(first_name))

#Exercise 3
first_name = 'Mufida'
last_name = 'Yaro'

if len(first_name) == len(last_name):
    print('The strings have equal lengths')
else:
    print('The two strings have different lengths')
    
#Exercise 4
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#Exercise 5
import math
radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius * radius
circum_of_circle = 2 * math.pi * radius

print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

#Exercise 6
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

#Exercise 7
import keyword
print(keyword.kwlist)
    
