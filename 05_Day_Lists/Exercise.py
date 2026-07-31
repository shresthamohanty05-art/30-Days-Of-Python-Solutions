# ## 💻 Exercises: Day 5

# ### Exercises: Level 1

# 1. Declare an empty list
print([])
# 2. Declare a list with more than 5 items
items= ['Apple' , 'Banana' , 'Coconut' , 'Drumstick' , 'Eggplant']
print(items)
# 3. Find the length of your list
print(len(items))
# 4. Get the first item, the middle item and the last item of the list
print(items[0])
print(items[len(items)//2])
print(items[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
data = ["Shrestha Mohanty" ,  20,  160, "not married","Odisha"]
print(data)
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]
# 7. Print the list using _print()_
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(items)//2])
print(it_companies[-1])
# 10. Print the list after modifying one of the companies
it_companies[1] = "High Radius"
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append("Google")
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2 , "Infosys")
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
# 14. Join the it_companies with a string '#;&nbsp; 
separator = "#; "
separator.join(it_companies)
print("#; ".join(it_companies))
# 15. Check if a certain company exists in the it_companies list.
print("Apple" in it_companies)
# 16. Sort the list using sort()
it_companies.sort() 
print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[3:])
# 19. Slice out the last 3 companies from the list
print(it_companies[:-3])
# 20. Slice out the middle IT company or companies from the list
n= len(it_companies)

if n%2 == 0:
    middle = it_companies[n//2-1 : n//2+1]
else:
    middle = it_companies[n//2]

print(middle)

# 21. Remove the first IT company from the list
print(it_companies[1:])
# 22. Remove the middle IT company or companies from the list
mid = len(it_companies)//2
i = it_companies[:mid] + it_companies[mid+1:]
print(i)
# 23. Remove the last IT company from the list
print(it_companies[:-1])
# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25. Destroy the IT companies list
# del it_companies
# print(it_companies)
# 26. Join the following lists:

#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end =  ['Node','Express', 'MongoDB']

final = front_end.__add__(back_end)
print(final)
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = final.copy()

index = full_stack.index("Redux")

full_stack.insert(index + 1, "Python")
full_stack.insert(index + 2, "SQL")

print(full_stack)
# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

# ```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```


# - Sort the list and find the min and max age
ages.sort()
print(ages)
# - Add the min age and the max age again to the list
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)
print(ages)
# - Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages)
if len(ages)%2==0:
    median = (ages[len(ages)//2 -1]+  ages[len(ages)//2])/2
    print(median)
else:
    median= ages[len(ages)//2]
    print(median)
# - Find the average age (sum of all items divided by their number )
avg = sum(ages)/len(ages)
print("Average: ", avg )
# - Find the range of the ages (max minus min)
range = max_age-min_age
print("Range: " , range)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
min_u = min_age - avg
max_u = max_age - avg
print(min_u)
print(max_u)
# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries =  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
if len(countries)%2 ==0:
    ind = len(countries)//2+1
    c1 = countries[:ind+1]
    c2= countries[ind+1:]
    print(c1)
    print(c2)
else:
    ind= len(countries)//2
    c1= countries[:ind+1]
    c2= countries[ind+1:]
    print(c1)
    print(c2)


