__author__ = 'arran'

import random
import csv
import sys

positions = {}

def get_random():
    #return random.randint(1,10)
    return (random.randint(1,10) - 5) / 10.0

# -35.2772
# 149.1292

with open("output.csv", "w") as output_csv:

    writer = csv.writer(output_csv)

    with open('words-sanitised.csv', 'rb') as input_csv:
            reader = csv.reader(input_csv, delimiter=',', quotechar="\"")

            writer.writerow(reader.next()) # Skip header row

            for index, row in enumerate(reader):
                if index < 1000: # Was using to limit earlier because it's slow.
                    words = []
                    print(index)
                    print(row[14])
                    lat = row[11]
                    long = row[12]

                    if lat:
                        if (lat, long) in positions:
                            print("duplicate on " + str(lat))
                            lat = float(lat) + get_random()
                            long = float(long) + get_random()
                        else:
                            positions[(lat, long)] = 1

                        writer.writerow(row[0:11] + [str(lat)] + [str(long)] + [row[13]] + [row[14]])


#for line in lines:
#    print(line)

