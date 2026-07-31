import math

## 💻 Exercises - Day 3

# 1. Declare your age as integer variable
# 2. Declare your height as a float variable
# 3. Declare a variable that store a complex number
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# ```py
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

age = 20
height = 5.3
var = 2+3j 

# print("Age: " , age)
# print("Height : " , height)
# print("Complex no: " , var)

# base = int(input("Enter base: "))
# height = int(input("Enter height : "))
# arear = 0.5*base*height

# print("Area of rectangle: ", arear)


# ```

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# ```py
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
# ```

# a = int(input("Side a: "))
# b = int(input("Side b: "))
# c = int(input("Side c: "))
# areat= a+b+c

# print("Area of triangle: " , areat)


# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# arear = length*width
# peri = 2*(length+width)

# print("Area: " , arear)
# print("Perimeter: ", peri)


# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# radius = int(input("Enter radius: "))
# areac= 2*3.14*radius
# peri= 3.14*radius*radius
# print("Circumference: ", peri)
# print(f"Area:  {areac:.2f}")


# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# m = 2
# c= -2

# print("Slope: ", m)

# y_int = (0,c)
# print("Y-intercept: " , y_int)

# x_int = (-c/m, 0)

# print("I-intercept: " , x_int)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
# x1, y1= 2,2
# x2, y2= 6, 10
# m = (y2-y1)/(x2-x1)
# print("slope: ", m)
# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("Distance: ", distance)

# 10. Compare the slopes in tasks 8 and 9.
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# a = 1
# b=6
# c=9
# x = (-b+math.sqrt(b**2-4*a*c))/(2*a) 
# y = x**2+6*x+9
# print("x: " , x)
# print("y: " , y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = "python"
b = "dragon"
# print("Length of python: " , len(a))
# print("Length of dragon: ", len(b))
# print(a==b)
# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon" )
# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.

print("_jargon_" in "_I hope this course is not full of jargon_")
# 15. There is no 'on' in both dragon and python

print(not("on" in "python" and "on" in "dragon") )

# 16. Find the length of the text _python_ and convert the value to float and convert it to string
print(len("_python_"))
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 8
print(num%2 == 0)
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3)
# 19. Check if type of '10' is equal to type of 10
print('10' == 10)
# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10 )
# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour = int(input("Enter total hours: "))
rate = int(input("Enter the rate: "))
pay = hour*rate
print("Pay : " , pay)