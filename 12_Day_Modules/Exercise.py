# ## 💻 Exercises: Day 12

# ### Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id. 
#    ```py
#      print(random_user_id()) 
#      '1ee33d'
#    ```

# import random
# def random_user_id():
#     characters = "abcdefghijklmnopqrstuvwxyz0123456789"
#     ans = ""
#     for i in range(7):
#         ans += random.choice(characters)
#     return ans
# print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
# ```py
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

# import random

# def random_user_id(num):
#     characters = "abcdefghijklmnopqrstuvwxyz0123456789"
#     ans = ""
#     for i in range(num):
#         ans += random.choice(characters)
#     return ans

# def user_id_gen_by_user():
#     num_of_char = int(input("Enter the number of characters: "))
#     num_of_id = int(input("Enter the number of IDs: "))

#     for i in range(num_of_id):
#               print(random_user_id(num_of_char)) 
# user_id_gen_by_user()             
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# ```

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
# ```py
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
# ```
import random
# def rgb_color_gen():
#       r = random.randint(0, 255)
#       g = random.randint(0, 255)
#       b = random.randint(0, 255)
#       return f"rgb({r}, {g}, {b})"
# print(rgb_color_gen())
      

# ### Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# 1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# 1. Write a function generate_colors which can generate any number of hexa or rgb colors.

# ```py
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
#    ```

import random
def generate_colors(type_is, num):
      colors = []
      if type_is == 'hexa':
            characters="0123456789abcdef"
            for i in range(num):
                  ans ="#"
                  for j in range(6):
                        ans += random.choice(characters)
                  colors.append(ans)
      elif type_is == 'rgb':
           for i in range(num):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            colors.append(f"rgb({r},{g},{b})")
      return colors

# type_is = input("Enter whether hex or rgba: ")
# num = int(input("Enter number of colors: "))
# print(generate_colors(type_is, num))
# ### Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
     random.shuffle(lst)
     return lst

print(shuffle_list([1, 2, 3, 4, 5, 6]))
# 1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def sev_num():
     num = []
     while len(num) < 7:
       n = random.randint(0, 9)
       if n not in num:
            num.append(n)
     return num
print(sev_num())
# 🎉 CONGRATULATIONS ! 🎉