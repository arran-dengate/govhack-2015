__author__ = 'arran'

# Imports the CSV file and does stuff.

import urllib2
import re
import csv
import sys
import requests
from requests.exceptions import HTTPError

def get_word_list(paragraphs):

    word_list = []

    for paragraph in paragraphs:
        inner_list = paragraph.split()

        for word in inner_list:
            word_list.append(word)

    return word_list

# Import file

# file = json.loads(open("data.json").read(), encoding="cp1252")

word_data = []
word_text = ""
counter = 0

with open("output.csv", "w") as output_csv:

    writer = csv.writer(output_csv)

    with open('data.csv', 'rb') as input_csv:
            reader = csv.reader(input_csv, delimiter=',', quotechar="\"")

            writer.writerow(reader.next() + ["Words"])
            #reader.next() # Skip the header row

            for index, row in enumerate(reader):
                if index < 100000: # Was using to limit earlier because it's slow.
                    counter += 1
                    words = []
                    url = row[1]
                    #print(url)
                    try:
                        response = urllib2.urlopen(url)
                        html = response.read()
                    except urllib2.HTTPError:
                        html = ""
                    text = re.findall("<p>.*</p>", html)

                    for item, paragraph in enumerate(text):

                        text[item] = re.sub("\<.{1,6}\>", " ", paragraph)      # Remove tags
                        text[item] = re.sub("\<a href=.{1,200}\>", " ", text[item]) # Remove hyperlinks (might del other stuff, could improve)
                        words.append(text[item])

                    word_data.append(get_word_list(words))

                    for list in word_data:
                        for word in list:
                            word_text = word_text + " " + word

                    #sys.exit()

                word_text = "\"" + word_text + "\""
                #print(word_text)
                writer.writerow(row + [word_text])
                word_data = []
                word_text = ""
                print(counter)






