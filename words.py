# For a list of words, print out each word on a separate line, 
# but in all uppercase. How can you change a word to uppercase? 
# Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. 
# (Don’t forget to add a docstring to your function!)

# this should print "HELLO", "HEY", "YO", and "YES"
        # print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
        #                 must_start_with={"h", "y"})

def print_upper_words (words):
    """prints out each word in a list in all uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(["cat", "dog", "bunny", "hippo", "dolphin"])



# Change that function so that it only prints words that 
# start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, 
# and it only prints words that start with one of those letters.

def print_upper_words_specific_letter (words, starts_with):
    """prints out each word in a list in all uppercase that starts with a specific letter"""
    for word in words:
        if word[0] == starts_with:
            print(word.upper())

print_upper_words_specific_letter(["cat", "dog", "bunny", "hippo", "dolphin"], starts_with="d")