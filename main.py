"""Quote gener"""

"""
Task: User enters a hash tag and based on that tag, the Python program must be able to generate quotes one after the other. If the program isn't able to find any quote with the given tag, it has to print "Quote with given hash tag isn't found".

Solution:

We need to use a data set for this task. The data set must contain quotes and tags that can be associated with each quote. The program can then search the data set for the user specified tag and if it finds any quote, it can print the quote. We can find a lot of data sets already in the internet uploaded by developers across various websites like github, kaggle, etc.
"""

import json


with open("dataset.json") as f:
    quote_list = json.loads(f.read())
    tag = input("Print tag: ")

    hasTag = False

    for q in quote_list:
        if tag in q['Tags']:
            print(f"\nQuote: {q['Quote']}\nAuthor: {q['Author']}")
            hasTag = True if not hasTag else None

    if not hasTag:
        print("Quote with given hash tag isn't found")
