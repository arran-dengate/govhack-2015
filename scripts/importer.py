__author__ = 'arran'

# Imports the JSON file and does stuff.

print("Hello world")

import json
import urllib2
import re


def get_word_list(paragraphs):

    word_list = []

    for paragraph in paragraphs:
        inner_list = paragraph.split()

        for word in inner_list:
            word_list.append(word)

    return word_list

# Import file

file = json.loads(open("data.json").read(), encoding="cp1252")

with open("output", "w") as outfile:
    json.dump(file, outfile, indent=4)

# Read each line and go scrape the website.

for index, line in enumerate(file):
    url = file[index]["URL"]
    response = urllib2.urlopen(url)
    html = response.read()
    text = re.findall("<p>.*</p>", html)

    file[index]["words"] = []

    # Remove HTML tags.

    for item, paragraph in enumerate(text):

        text[item] = re.sub("\<.{1,6}\>", " ", paragraph)      # Remove tags
        text[item] = re.sub("\<a href=.{1,200}\>", " ", text[item]) # Remove hyperlinks (might del other stuff, could improve)

        #print(file[index]["words"])
        file[index]["words"].append(text[item])



    file[index]["words"] = get_word_list(file[index]["words"])

    print(file[index]["words"])



