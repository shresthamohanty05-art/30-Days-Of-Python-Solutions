# ## 💻 Exercises: Day 13

# 1. Filter only negative and zero in the list using list comprehension
#    ```py
#    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
#    ```
  
number = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zer = [num for num in number if num<=0 ]
print(neg_zer)
# 2. Flatten the following list of lists of lists to a one dimensional list :

#    ```py
#    list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    ```
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for rows in list_of_lists for num in rows]
print(flat)

# 3. Using list comprehension create the following list of tuples:
#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```

n = [(i, i**0 , i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(n)

# 4. Flatten the following list to a new list:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#    ```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
f = [c for row in countries for l in row  for c in l]
print(f)
#    output:
# 5. Change the following list to a list of dictionaries:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
    {
        'country': country.upper(),
        'city': city.upper()
    }
    for l in countries
    for country, city in l
]

print(result)
# 6. Change the following list of lists to a list of concatenated strings:
#    ```py
#    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result1 = [f"{first} {second}" for a in names for first, second in a]
print(result1)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)

print(slope(1, 2, 3, 4))

y_intercept = lambda x, y, m: y - m * x

print(y_intercept(1, 3, 1))

# 🎉 CONGRATULATIONS ! 🎉