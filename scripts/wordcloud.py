import random

# The 'summarise' method takes a list of strings as input.
# It will output a dictionary of words based on the wordcloud algorithm.

def summarise(input):

    output = [] # Initialise empty list

    for word in input:
        output.append({"text":word, "weight":1}) # Create a dictionary for each word, with the word itself and the frequency.

    return output

# The text below is a technique often used in Python.
# If the script is being run directly, it runs some tests. as shown.
# (If script is being used by another script, the code below will not be run.)

if __name__ == "__main__":

    results = summarise(['Fire', 'Flood', 'Drought', 'Hail'])
    print(results)

    # Desired output is a list of dicts, like so:
    # [{"text": "coffee", "weight": 20296.0},
    #  {"text": "love", "weight": 15320.0}, {"text": "day", "weight": 6860.0},
    #  {"text": "like", "weight": 5521.0}]