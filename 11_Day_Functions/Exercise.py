import math

# ## 💻 Exercises: Day 11

# ### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a+b

print(add_two_numbers(3,4))
# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle(r):
    return 3.14*r**2

print(area_of_circle(3))
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
# n = int(input("Enter no of parameter: "))


# def add_all_nums(n):
#     l= []
#     sum=0
#     for i in range(n):
#         i = int(input("Enter number : "))
#         l.append(i)
#         sum+= i 
    
#     return sum

# print(add_all_nums(n))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.

def convert_celsius_to_farheinheit(t):
    f = (t*(9/5))+32
    return f

print(convert_celsius_to_farheinheit(37))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    Autumn = ['September' , 'October' , 'November']
    Winter = ['December' , 'January' , 'February']
    Spring = ['March' , 'April' , 'May']
    Summer = [ 'June', 'July', 'August']


    if month in Autumn:
     print("Autumn season!")
    elif month in Winter:
     print("Winter season!")
    elif month in Spring:
     print("Spring season!")
    else:
     print("Summer season!")

# month = input("Enter a month: ")
# check_season(month)
# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Example
print(calculate_slope(2, 3, 6, 11))
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
def solve_quadratic_eqn(a,b,c):
   x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
   x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
   print(f"Solutions are {x1} and {x2}")

solve_quadratic_eqn(2,27,3)
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(l):
   for i in l:
      print(i)

list_u = ['apple' , 'banana' , 'carrot' , 'drumstick']
print_list(list_u)
   
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
# ```

def reverse_list(arr):
   arr_reversed = []
   i = len(arr)-1
   while i>-1:
      arr_reversed.append(arr[i])
      i -= 1
   return arr_reversed

arr = ['A' , 'B' , 'c']
reversed = reverse_list(arr)
print(reversed)
# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l):
   l2 = []
   for i in l:
      cap = i
      l2.append(cap.capitalize())
   return l2

print(capitalize_list_items(['apple', 'banana', 'mongoose' , 'snake']))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# ```
def add_item(l3, item):
   l3.append(item)
   return l3

l3 = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(l3, 'Meat'))

l4 = [1, 2, 3, 4]
print(add_item(l4, 5))



# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```
def remove_items(l3, item):
   l3.remove(item)
   return l3

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_items(food_stuff, 'Tomato'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# ```
def sum_of_numbers(num):
   s=0
   for i in range(num+1):
      s += i
   return s

print(sum_of_numbers(100))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
   s=0
   for i in range(num+1):
      if i%2 !=0:
          s += i
   return s

print(sum_of_odds(100))
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
   s=0
   for i in range(num+1):
      if i%2 ==0:
          s += i
   return s

print(sum_of_even(100))

# ### Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ```

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
   if num==1 or num==0:
      return 1
   return num*factorial(num-1)

print(factorial(5))
# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def is_empty(p):
   if len(p) == 0:
      return True
   else:
      return False
   
P=[]
print(is_empty(P))
# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(l):
   mean = sum(l)/len(l)
   return mean

print(calculate_mean([1,2,3,4,5]))

def calculate_median(l):
   l.sort()
   n = len(l)

   if n%2 !=0:
      return l[n//2]
   else:
      return (l[n//2 -1]+l[n//2])/2
print(calculate_median([1,2,3,4,5]))


def calculate_mode(lst):
    freq = {}

    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    mode = max(freq, key=freq.get)

    return {'mode': mode, 'count': freq[mode]}

print(calculate_mode([2, 3, 5, 6, 2, 3, 3, 8]))


def range_u(lst):
   return max(lst) - min(lst) 

print(range_u([1, 2, 3, 4, 5]))

def calculate_variance(lst):
   mean = calculate_mean(lst)

   total =0

   for num in lst:
      total += (mean-num)**2
   
   var = total/len(lst)
   return var

print(calculate_variance([2, 4, 6, 8]))
# 1. Write a function called _greet_ which takes a default argument, _name_. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

# ```py
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
# ```

def greet(name='Guest'):
   print(f'Hello, {name}!')

greet()
greet("shrestha")

# 1. Create a function called _show_args_ to take an arbitrary number of named arguments and print their names and values.
#    ```py
#    show_args(name="Alice", age=30, city="New York")
#    # Received: name: Alice, age: 30, city: New York
#    show_args(name="Bob", pet="Fluffy, the bunny")
#    # Received: name: Bob, pet: Fluffy, the bunny
#    ```

def show_args(**kwargs):
   print(kwargs)

show_args(name="Alice", age=30, city="New York")


# ### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
   if num<2 :
      return False
   
   for i in range(2, int(num**0.5) + 1):
      if num%i ==0 :
         return False

   return True

print(is_prime(7))


# 1. Write a functions which checks if all items are unique in the list.
def unique_items(lst):
    for i in lst:
       if lst.count(i) > 1:
          return False
    return True
print(unique_items([1, 2, 6, 9, 4, 7, 3]))
# 1. Write a function which checks if all the items of the list are of the same data type.
def check(lst):
   first_type = type(lst[0])

   for item in lst:
      if type(item) != first_type:
         return False

   return True

print(check([1, 4, 8, "Harry"]))


# 1. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    return variable.isidentifier()

print(is_valid_variable("first_name"))     # True
print(is_valid_variable("first-name"))     # False
print(is_valid_variable("123name"))        # False
print(is_valid_variable("_age"))           # True
print(is_valid_variable("for"))            # True

# 1. Go to the data folder and access the countries-data.py file.
from countries_data import countries_data

from collections import Counter
# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(n):
    language_count = Counter()

    for country in countries_data:
        language_count.update(country["languages"])

    return language_count.most_common(n)

print(most_spoken_languages(10))
# # - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(n):
    countries = []

    for country in countries_data:
        countries.append((country["name"], country["population"]))

    countries.sort(key=lambda x: x[1], reverse=True)

    return countries[:n]

print(most_populated_countries(10))