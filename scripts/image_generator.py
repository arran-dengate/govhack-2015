import csv
import TagCloud as tc
import wordcloud as wc
import random

with open("output.csv", "w") as output_csv:

    writer = csv.writer(output_csv)

    with open('words-sanitised-jittered.csv', 'rb') as input_csv:
            reader = csv.reader(input_csv, delimiter=',', quotechar="\"")

            writer.writerow(reader.next() + ["Billboards"]) # Skip header row

            for index, row in enumerate(reader):
                if index < 100000:

                    writer.writerow(row + [str.zfill(str(index), 4) + ".png"])
                    words = row[14]
                    summarised_words = wc.summarise(words, random.randint(7,20))
                    #print(summarised_words)
                    t = tc.TagCloud()
                    t.draw(summarised_words, "images/" + str.zfill(str(index), 4) + ".png")
                    print(index)




