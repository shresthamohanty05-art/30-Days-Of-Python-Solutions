# ## 💻 Exercises: Day 8

# 1. Create  an empty dictionary called dog

dog = {}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary

dog.update({
    'name': 'Tommy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 3
})

print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : "Shrestha",
    'last_name' : "Mohanty",
    'gender' : "Female" ,
    'age' : 20, 
    'marital status' : "unmarried" , 
    'skills' : ['Java' , 'Python' , 'Webdev' , 'VLSI'],
    'country' : "India" ,
    'city' : "Cuttack" ,
    'address' : "Satichoura"
}

print(student)

# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))
    
# 6. Modify the skills values by adding one or two skills
skills.append('SQL')
skills.extend(['MongoDB' , 'Nodejs'])
print(skills)
# 7. Get the dictionary keys as a list
key =[]
val=[]
for keys in student:
    key.append(keys)
    val.append(student[keys])

print(key)
print(val)

print(key)
# 8. Get the dictionary values as a list
print(val)
# 9. Change the dictionary to a list of tuples using _items()_ method
ans = list(student.items())
print(ans)
# 10. Delete one of the items in the dictionary
del student['address']
# 11. Delete one of the dictionaries
del dog
