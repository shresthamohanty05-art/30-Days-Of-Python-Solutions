import math


# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# 3. Declare a first name variable and assign a value to it
# 4. Declare a last name variable and assign a value to it
# 5. Declare a full name variable and assign a value to it
# 6. Declare a country variable and assign a value to it
# 7. Declare a city variable and assign a value to it
# 8. Declare an age variable and assign a value to it
# 9. Declare a year variable and assign a value to it
# 10. Declare a variable is_married and assign a value to it
# 11. Declare a variable is_true and assign a value to it
# 12. Declare a variable is_light_on and assign a value to it
# 13. Declare multiple variable on one line

first_name = "Shrestha"
last_name = "Mohanty"
full_name = "Shrestha Mohanty"
country = "India"
city = "Cuttack"
age = 20
year =2026
is_true = True
is_light_on = True


first_name, last_name, full_name, country, city, age , year, is_true, is_light_on = "Shrestha" , "Mohanty" , "Shrestha Mohanty" , "India" , "Cuttack", 20, 2026, True, True

# print("First name: " , first_name)
# print("Full name : " , full_name) 
# print("Country: " , country)
# print("City: " , city)
# print("Age: " , age)
# print("Year: " , year)
# print("Is light on ? : ", is_light_on) 

### Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function
# 2. Using the _len()_ built-in function, find the length of your first name
# 3. Compare the length of your first name and your last name
# 4. Declare 5 as num_one and 4 as num_two
# 5. Add num_one and num_two and assign the value to a variable total
# 6. Subtract num_two from num_one and assign the value to a variable diff
# 7. Multiply num_two and num_one and assign the value to a variable product
# 8. Divide num_one by num_two and assign the value to a variable division
# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
# 12. The radius of a circle is 30 meters.
#     1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
#     2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
#     3. Take radius as user input and calculate the area.
# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# 14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

# print(type(first_name))
# print(type(last_name))
# print(type(full_name))
# print(type(country))
# print(type(city))
# print(type(age)) 
# print(type(year))
# print(type(is_true))
# print(type(is_light_on))

# print("Length of first name : " , len(first_name))

# if (len(first_name) > len(last_name)):
#     print("First name is longer")

# elif len(first_name) < len(last_name):
#     print("Last name is longer")

# else:
#     print("Both have same length")

num_one = 5
num_two = 4
# total = num_one + num_two
# print("Total: " , total)

# diff= num_one - num_two
# print("Difference : " , diff)

# product = num_one * num_two
# division = num_one/num_two
# mod = num_one % num_two

# print("Product: " , product)
# print("Difference: " , diff)
# print("Modulus: " , mod)

# exp = num_one**num_two
# floor = num_one// num_two

# print("Exponential: " , exp)
# print("Floor division: ", floor)

radius = 30
area= math.pi * radius**2 
circum = 2*math.pi*radius 
# print("Area: " , area)
# print("Circumference: " , circum)

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = int(input("Enter age: "))

print(first_name)
print(country)
print(age)
