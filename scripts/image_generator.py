
import csv
import TagCloud as tc
import wordcloud as wc

with open('words-sanitised.csv', 'rb') as input_csv:
        reader = csv.reader(input_csv, delimiter=',', quotechar="\"")

        for index, row in enumerate(reader):
            if index < 80000:

                words = row[14]
                summarised_words = wc.summarise(words, 5)
                t = tc.TagCloud()
                t.draw(summarised_words, "images/" + str.zfill(str(index), 4) + ".png")
                print(index)




