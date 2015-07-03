import random

# The 'summarise' method takes a list of strings as input.
# It will output a dictionary of words based on the wordcloud algorithm.

def summarise(input):

    output = {} # Initialise empty dictionary

    for word in input:
        output[word] = 1 # In the dictionary, set the frequency of each supplied item to 1

    return output

# The text below is a technique often used in Python.
# If the script is being run directly, it runs some tests. as shown.
# (If script is being used by another script, the code below will not be run.)

if __name__ == "__main__":

    results = summarise(['Fire', 'Flood', 'Drought', 'Hail'])
    print(results)