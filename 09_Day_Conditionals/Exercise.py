# ## 💻 Exercises: Day 9

# ### Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```

# age = int(input("Enter your age: "))
# if age>= 18:
#     print("You are old enough to drive")
# else:
#     print(f"You need {18-age} more years to learn to drive")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```



# 3. Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
# Output:

# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a>b :
#     print(f"{a} is greater than {b}")
# elif a<b:
#      print(f"{a} is smaller than {b}")
# else:
#     print("Both are equal")

# ### Exercises: Level 2

#    1. Write a code which gives grade to students according to theirs scores:

#     ```sh
#     90-100, A
#     80-89, B
#     70-79, C
#     60-69, D
#     0-59, F
#     ```

# mark = int(input("Enter your marks: "))

# if mark>=90 and mark<100 :
#     print('A')
# elif mark>=80 and mark<90 :
#     print('B')
# elif mark>=70 and mark<80 :
#     print('C')
# elif mark>=60 and mark<70 :
#     print('D')
# else:
#     print('F')

#    2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

# Autumn = ['September' , 'October' , 'November']
# Winter = ['December' , 'January' , 'February']
# Spring = ['March' , 'April' , 'May']
# Summer = [ 'June', 'July', 'August']

# month = input("Enter a month: ")

# if month in Autumn:
#     print("Autumn season!")
# elif month in Winter:
#     print("Winter season!")
# elif month in Spring:
#     print("Spring season!")
# else:
#     print("Summer season!")

#    3. The following list contains some fruits:

#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```

#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print(f"{fruit} already exists in the list")
else:
    fruits.append(fruit)
    print(f"Modified list: {fruits}")

# ### Exercises: Level 3

#    1. Here we have a person dictionary. Feel free to modify it!

# ```py
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# ```