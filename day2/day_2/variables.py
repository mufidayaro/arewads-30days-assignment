#Exercise: Level 1
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
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Mufida', 'Yaro', 'Mufida Yaro', 'Nigeria', 'Kano', 21, 2023, False, True, True

print(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

#Level 2 Exercise 1:Check the data type of all your variables using type() built-in function
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

#Exercise 2:Using the len() built-in function, find the length of your first name
print(len(first_name))
#Exercise 3:Compare the length of your first name and your last name
print(len(last_name))
#Exercise 4:Declare 5 as num_one and 4 as num_two
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

#Exercise 5:The radius of a circle is 30 meters.
"""Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area."""

import math
radius = float(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius * radius
circum_of_circle = 2 * math.pi * radius

print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

#Exercise 6:Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

#Exercise 7:Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
import keyword
print(keyword.kwlist)
