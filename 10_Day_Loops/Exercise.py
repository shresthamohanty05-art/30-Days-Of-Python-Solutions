# ## 💻 Exercises: Day 10

# ### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i , "\n")

i=0
while i<11:
    print(i, "\n")
    i +=1


# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

i=10
while i>-1:
    print(i)
    i-=1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```

for i in range(7):
    for j in range(i):
        print("#", end="")
    print()

print("\n")

# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

for i in range(8):
    for j in range(8):
        print("#", end="")
    print()


print("\n")


# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
l = ['Python', 'Numpy' , 'Pandas' , 'Django' , 'Flask']

for i in l:
    print(i, end=", ")

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 ==0:
        print(i)
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2 !=0:
        print(i)


# ### Exercises: Level 2

# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

# ```sh
# The sum of all numbers is 5050.
# ```

sum =0
for i in range(101):
    sum += i
print(f"Sum of all numbers : {sum}")
# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#    ```sh
#    The sum of all evens is 2550. And the sum of all odds is 2500.
#    ```
evensum=0
oddsum=0

for i in range(101):
    if i%2==0:
        evensum += i
    else:
        oddsum +=i

print(f"Even sum : {evensum}")
print(f"Odd sum : {oddsum}")

# ### Exercises: Level 3

# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

land= []

for country in countries:
    if 'land' in country:
        land.append(country)

print("Countries having 'land' : " , land)

# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
i = len(fruit)-1 ;
rev = []
while i>=0:
    rev.append(fruit[i])
    i-=1

print(f"Reversed fruit list : {rev}")
# 1. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.
#    1. What are the total number of languages in the data
from countries_data import countries_data

language_set = set()

for country in countries_data:
    for language in country["languages"]:
        language_set.add(language)

print("Total number of languages:", len(language_set))
#    2. Find the ten most spoken languages from the data
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(
    language_count.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Top 10 most spoken languages:")

for language, count in sorted_languages[:10]:
    print(language, "-", count)
#    3. Find the 10 most populated countries in the world
sorted_population = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)

print("Top 10 most populated countries:")

for country in sorted_population[:10]:
    print(country["name"], "-", country["population"])
