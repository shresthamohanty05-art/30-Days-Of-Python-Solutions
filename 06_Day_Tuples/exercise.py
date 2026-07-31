# ## 💻 Exercises: Day 6

# ### Exercises: Level 1

# 1. Create an empty tuple
t = ()
print(t)
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Shrestha','Tisya', 'Tapasya',)
brothers = ( 'Ayush', 'Shourya',  'Anshuman')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters+brothers
# 4. How many siblings do you have?
print("I have ", len(siblings), " siblings")
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family = siblings + ('Shakti' , 'Aparna')
print("Family: " , family)

# ### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
*siblings, father , mother = family
print(siblings)
print(father)
print(mother)
# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana')
vegetable = ('brocolli' , 'potato')
animal_prod = ('milk' , 'egg')
food_stuff_tp = fruits + vegetable+ animal_prod

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list 
food_stuff_lt = list(food_stuff_tp)
# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = food_stuff_lt[len(food_stuff_lt)//2-1: len(food_stuff_lt)//2+1]
print(mid)
# 1. Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[3:-3])
# 1. Delete the food_stuff_tp tuple completely
# del food_stuff_tp
# print(food_stuff_tp)
# 1. Check if an item exists in  tuple:
print(food_stuff_tp.__contains__('potato'))

nordic_countries = ('Denmark' , 'Finland' , 'Iceland' , 'Norway' , 'Sweden')
# - Check if 'Estonia' is a nordic country
print('Is Estonia a nordic country?')
print('Estonia' in nordic_countries)
# - Check if 'Iceland' is a nordic country
print('Is Iceland a nordic country?')
print('Iceland' in nordic_countries)
#   ```py
#   nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#   ```
