
# ## 💻 Exercises: Day 19

# ### Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#    1) Read obama_speech.txt file and count number of lines and words

# with open('obama_speech.txt' , 'r' ) as f:
#     lines = f.readlines()
#     print(len(lines))

#     words = 0
#     for line in lines:
#         words += len(line.split())
#     print(words)

      
#    2) Read michelle_obama_speech.txt file and count number of lines and words

# with open('michelleobama_speech.txt' , 'r' ) as f:
#     lines_1 = f.readlines()
#     print(len(lines_1))

#     words_1 = 0
#     for line_1 in lines_1:
#         words_1 += len(line_1.split())
#     print(words_1)
#    3) Read donald_speech.txt file and count number of lines and words
# with open('trump_speech.txt' , 'r' ) as f:
#     lines_2 = f.readlines()
#     print(len(lines_2))

#     words_2 = 0
#     for line_2 in lines_2:
#         words_2 += len(line_2.split())
#     print(words_2)
#    4) Read melina_trump_speech.txt file and count number of lines and words
# with open('melinatrump_speech.txt' , 'r' ) as f:
#     lines_3 = f.readlines()
#     print(len(lines_3))

#     words_3 = 0
#     for line_3 in lines_3:
#         words_3 += len(line_3.split())
#     print(words_3)

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

#    ```py
#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 10))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic'),
#    (24, 'Spanish'),
#    (9, 'Russian'),
#    (9, 'Portuguese'),
#    (8, 'Dutch'),
#    (7, 'German'),
#    (5, 'Chinese'),
#    (4, 'Swahili'),
#    (4, 'Serbian')]

#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 3))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic')]
#    ```
    

    

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

#    ```py
#    # Your output should look like this
#    print(most_populated_countries(filename='./data/countries_data.json', 10))

#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000},
#    {'country': 'Indonesia', 'population': 258705000},
#    {'country': 'Brazil', 'population': 206135893},
#    {'country': 'Pakistan', 'population': 194125062},
#    {'country': 'Nigeria', 'population': 186988000},
#    {'country': 'Bangladesh', 'population': 161006790},
#    {'country': 'Russian Federation', 'population': 146599183},
#    {'country': 'Japan', 'population': 126960000}
#    ]

#    # Your output should look like this

#    print(most_populated_countries(filename='./data/countries_data.json', 3))
#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000}
#    ]
#    ```
import json

# def most_populated_countries(countries_data, n):
#     with open(countries_data, 'r', encoding='utf-8') as f:
#         countries = json.load(f)

#     countries.sort(key=lambda country: country['population'], reverse=True)

#     return countries[:n]


# print(most_populated_countries('countries_data.json', 10))
# print(most_populated_countries('countries_data.json', 3))

# ### Exercises: Level 2

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
with open("email_exchange_big.txt" , 'r') as f:
   text = f.read()
   l = []
   for word in text.split():
      word = word.strip('.,')
      if word.endswith('.com'):
         l.append(word)


print(l)

# 2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

# ```py
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]'

def find_most_common_words(file, n):
   with  open(file , 'r') as f:
       text = f.read()



   words = text.split()

   word_count = {}
   for word in words:
       if word in word_count:
           word_count[word] += 1
       else:
           word_count[word] = 1

   result = []

   for word, count in word_count.items():
    result.append((count, word))

   result.sort(reverse=True)
   return result[:n]

print(find_most_common_words("sample.txt" , 10))






#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# ```

# 3. Use the function, find_most_frequent_words to find:
#    1) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
#    2) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#    3) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
#    4) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
# 4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory
# 5. Find the 10 most repeated words in the romeo_and_juliet.txt
# 6. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
#    1) Count the number of lines containing python or Python
#    2) Count the number lines containing JavaScript, javascript or Javascript
#    3) Count the number lines containing Java and not JavaScript

# 🎉 CONGRATULATIONS ! 🎉