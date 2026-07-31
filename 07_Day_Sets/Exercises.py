## 💻 Exercises: Day 7

# ```py
# # sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# ``

# ### Exercises: Level 1

# 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(('Infosys' , 'TCS' , 'High Radius'))
print(len(it_companies))
# 4. Remove one of the companies from the set it_companies
# it_companies.remove('Apple')
print(len(it_companies))
# 5. What is the difference between remove and discard
#Since Apple is now absent if i try to discard it cant discard but unlike remove it wont throw any error 
it_companies.discard('Apple')
# it_companies.remove('Apple')

# ### Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
C = A.union(B)
print(C)
# 2. Find A intersection B
D = A.intersection(B)
print(D)
# 3. Is A subset of B
print(A.issubset(B))
# 4. Are A and B disjoint sets
print(A.isdisjoint(B))
# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))
# 6. What is the symmetric difference between A and B
E = A.symmetric_difference(B)
print(E)
# 7. Delete the sets completely
del A
del B

# print(A)   # This will give NameError because A has been deleted.
# print(B) 

# ### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
if len(age) > len(ages) :
    print("List is bigger")
else:
    print("Set is bigger")

# 2. Explain the difference between the following data types: string, list, tuple and set
# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sen = "I am a teacher and I love to get inspired and to teach people"
sen1 = sen.split(" ");
print(len(sen1))
sen2 = set(sen1);
print(len(sen2))



