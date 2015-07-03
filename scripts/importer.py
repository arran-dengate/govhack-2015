__author__ = 'arran'

# Imports the JSON file and does stuff.

print("Hello world")

import json
import urllib2
import re

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
    for index, paragraph in enumerate(text):
        # Get rid of HTML tags.
        text[index] = re.sub("\<.{1,6}\>", "", paragraph)      # Remove tags
        text[index] = re.sub("\<a href=.{1,200}\>", "", text[index]) # Remove hyperlinks (might del other stuff, could improve)
        #print(paragraph)
    print(text)

