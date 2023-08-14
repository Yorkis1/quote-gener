"""Quote gener
Task: User enters a hash tag and based on that tag, the Python program must be able to generate quotes one after the other. If the program isn't able to find any quote with the given tag, it has to print "Quote with given hash tag isn't found".

Solution:

We need to use a data set for this task. The data set must contain quotes and tags that can be associated with each quote. The program can then search the data set for the user specified tag and if it finds any quote, it can print the quote. We can find a lot of data sets already in the internet uploaded by developers across various websites like github, kaggle, etc.

"""

import json

with open("dataset.json") as f:
    quote_list = json.loads(f.read())

tag = input("Enter a tag: ")
dictionary = {}

for q in quote_list:
    if tag in q['Tags']:
        dictionary[q['Author']] = q['Quote']

if len(dictionary) != 0:
    count = 1
    for key, val in dictionary.items():
        print(f"\nQuote: {val}\nAuthor: {key}")

        if len(dictionary) > count:
            count += 1
            if input("\nNext(Y/N): ") == "Y" or "y":
                continue
        else:
            break
else:
    print("\nSorry, we couldn't find any quote with given tag")