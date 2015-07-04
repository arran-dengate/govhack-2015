import random
import re

# The 'summarise' method takes a string as input.

def summarise(input, max):

    wordList = re.sub("[^\w]", " ",  input).split();

    mid = {} # Initialise empty list

    for word in wordList:
        mid[word] = 0

    for word in mid:
        mid[word] = input.count(word)

    # Create a dictionary for each word, with the word itself and the frequency.
    mid2 = [] # Initialise empty list

    for word in mid:
        mid2.append({"text":word, "weight":mid[word]})

    # blackList = ['is', 'at', 'do', 'so', 'the', 'no', 'a', 'The', 'when', 'if'] #useless words to remove from story

    #read from text
    with open("StopWordList.txt") as f:
        contents = f.read()
        # print(type(contents))
        contents = contents.split("\t")
    newContents = []
    for word in contents:
        split_words = word.split("\n")
        for w in split_words:
            w = w.strip("'")
            w = w.strip('"')
            w = w.lower()
            newContents.append(w)

    blackList = [x.strip() for x in newContents]

    #remove blacklisted words
    output = []
    for entry in mid2:
        if not entry['text'].lower() in blackList:
            output.append(entry)

    newList = []

    #sort list and re-order with most frequent words first
    newList = sorted(output, key=lambda k: k['weight'], reverse=True)

    #remove all but most frequent 5 words
    del newList[max:]

    return newList


# The text below is a technique often used in Python.
# If the script is being run directly, it runs some tests. as shown.
# (If script is being used by another script, the code below will not be run.)

if __name__ == "__main__":

    #read .csv file, or many .csv files, read in final column. summarise() column and print output as separate file

    mystr = " How would you like to live in a house that generates more electricity than it uses, you never have to turn on the air conditioner and heater, and it doesn't cost that much more than a regular house to build. Step inside Mittagong's Greeny Flat. I'd been living in the United States for 20 years in Montana where it gets down to minus 50 degrees celsius at times, so energy efficiency is a whole different kettle of fish, he says. Coming back here it seems really easy to do this. After returning to Australia, he sized up his mother's backyard and designed and built his Greeny Flat - a two bedroom fully functional unit that is now producing almost twice as much energy as it's using. He started with two main goals - to make it energy positive, and to show people that it can be affordable. My philosophy is, regardless of what you think about global warming, at some point we have to learn to live without fossil fuels, because they won't last forever. This experiment is to see if we can do it now, and if we can, why not do it? The flat is meticulously designed to capitalise on available daylight for solar energy and natural heating, while shade and the floor slab will help regulate the inside temperate during the hottest and coldest parts of the year. There's a water tank out the back to capture rain water, and last week the flat underwent a blower door test by University of Wollongong researchers to ensure it was airtight. He and his girlfriend have just spent their first month living in the flat. Early indications are that it will work really well, Andy says. Winter will be the real test, but I have no doubts in the summer we'll make more energy than we're using. Just over the last week since we had our solar panels installed we're making twice the energy we're using. He says it's likely his mother will move into the flat in her later years, so he also designed the house to make it compatible for the elderly. There are ramps, as well as sufficient door space to move a walking frame through, the indoor and outdoor space is low maintenance, and the corrugated iron cladding outside means not a drop of paint has been used outside. I've been working on this full time for a year now in designing, planning and building it. I've just finished it and I'm about to take a holiday, but when I get back I'll be thinking about what I'll do for a crust. The Greeny Flat doesn't only just stand out for its striking metal design, it's miles more energy efficient than most houses built in Australia today. Andy says when he left the country 20 years ago, Australia was ahead of the US on energy efficient housing design. Now we have fallen behind, and we are even further behind Europe, where houses need to be designed to withstand extreme temperatures and make use of natural energy options. We're an energy producing nation and we have cheap energy but we're all starting to realise energy prices are going up. Threats of global warming are making people conscious of the energy we use and the carbon we produce. You can stay up to date on how the Greeny Flat is performing with Andy's blog ."
    #mystr = " When the railway reached Nimmitabel in 1912 it connected the remote Monaro town with the rest of the world. The railway was vital to the town and affected every aspect of life and work. Nancy Burke, the station master's daughter, remembers the locomotives as living things. Local farmer Ian Blyton recalls, Even the Canberra road in 1950 was still a dirt road. He said that vehicles created three ruts: two on the outside and one in the middle, and both north and south bound traffic used the rut in the middle of the road for their inside wheels. Between those wheel tracks was just a dust pile, he said, It was a wild road. He said it wasn't until the 1950s that trucks with stock crates were being used to transport sheep, but that before then if you wanted to send sheep for sale you had to walk them there. So the coming of the rail meant that sheep could be loaded and shipped to any of the saleyards between Nimmitabel and Sydney. Nancy Burke, whose father was the station master at Nimmitabel during the 1940s, recalls how the station was the hub of the community. Special trains would be put on to take people to race meetings, show days, and football matches as far away as Cooma, Queanbeyan, and Goulburn. And Bombala replaced Cooma as Nimmitabel's main service centre after the train line reached there in 1921. The Sydney mail train passed through Nimmitabel to Bombala in the morning and returned through Nimmitabel in the afternoon on the way back through Cooma - perfect timing for a day in Bombala. You had time to do some shopping and then have lunch, said Nancy, And then catch the train back at about half past two and you were back here at five o'clock." "I love the trains, I really do, she said of the old steam trains, The smell of them and because they were live. They're living things. Diesels no. They're dead things. The steams. The old 32s and 36s. Oh, wonderful. Listen to the attached audio for the full interview with Kevin and Nancy Burke. ' + $(this).attr('title') + '"

    mystr = " News, stories, people and pictures of 2014 in the South West Also in January, social media played a pivotal part in exposing what appeared to be a fraud involving home ultrasounds. Shicara Linnett of Bunbury discovered that photos she believed were of her daughter, were identical to other photos on the internet. A woman was charged with making false and misleading representations over the matter. In March, as Belgian buglers visited Yarloop to play the last post. The occasion honoured those who died defending Belgium at the Menin Gate on the way to Ypres. There were several anniversaries throughout the region, including 80 years of service by the Manjimup CWA in May. Later in the year, Northcliffe celebrated 90 years . Townsfolk brought out the finery for the traditional ball and dressed up for a parade down the main street on the following day. In May, Brunswick received the sad news that some processing at the historic Brunswick creamery would move to Perth and some people were made redundant. Judy Talbot worked there in the 50s. Just before Christmas, a fire broke out at Nannup Timber Processing in the kiln heater which eventually destroyed kilns and infrastructure. It may be the end of January before some dryers can be functional again and some workers may lose work. In Mid-year, probably the biggest event of 2014 was the Cowaramup attempt on the world record for the most number of people dressed as a cow in the one place. There were smiles and laughter everywhere as 1,352 black and white clad people were herded into the pen for the official count. The world record was broken. In August, sightseers turned out when heavy rains flooded the Preston River . The flooding was evident in Donnybrook where orchards and bridges were inundated. The following month, the news that a convicted child sex offender was the father of a little girl born by surrogacy shocked the community. Griffin Coal continued to struggle as parent company Lanco Infratech faced its own financial difficulty. Problems surfaced again later in the year when Carna Civil terminated its contract with Griffin and removed machinery from the mine. In October, Vasse went to the polls following the resignation of Troy Buswell. Liberal Libby Mettam replaced him. A new staff member at Bunbury Police station attracted a lot of attention in April. Geoffrey the police dog and his handler First Class Constable Jake Carruthers proved their worth even before taking up official duties. That month, there was also good news for the Babaie family who came to Australia from Iraq. In 2013, the refugee family found a welcome in Collie and in April received the news that they would be granted a further bridging visa. A year of art The artist year began with the South West survey, the annual exhibition displaying the best from the region. One of the loveliest images was Masked Owl by Kay Gibson. In April, CinefestOz announced a film prize of $100,000, the biggest in Australia. Joel Edgerton was one of the festival guests. Sophie Armstrong of Balingup took out the Cine-snaps short film competition with Kinetic happiness. In film, Leslie Rouvray had a wonderful career as a makeup artist in film and television. One of her specialities is making fake blood It's even edible! The Leschenault Men's Shed were busy making things for the community and at the same time providing a space for men to share, talk and resolve. The movement has gained ground in the South West with a new shed opening in Bunbury. Finally, enjoy some images of the reasons so many people love to live here: the beaches, the rivers and the forests."

    # wordList = re.sub("[^\w]", " ",  mystr).split();

    # for i in range(0,1000):
    results = summarise(mystr, 5)

   # results = summarise(['Fire', 'Flood', 'Drought', 'Hail', 'Hail', 'Hail', 'Flood', 'Entertainment'])
   #  results = summarise(['Fire', 'Flood', 'Drought', 'Hail'])
    for item in results:
        #remove useless/irrelevant words
        print(item)
    #print(results)


    #print output to file

    # text_file = open("Output.txt", "w")
    # text_file.write()

    # Desired output is a list of dicts, like so:
    # [{"text": "coffee", "weight": 20296.0},
    #  {"text": "love", "weight": 15320.0}, {"text": "day", "weight": 6860.0},
    #  {"text": "like", "weight": 5521.0}]

