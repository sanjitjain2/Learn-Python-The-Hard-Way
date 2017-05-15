def break_words(stuff):
    """this function will break up words for us"""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """sort the words"""
    return sorted(words)
    
def print_first_word(words):
    """prints the first word after popping it off."""    
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints last word after popping it off."""
    word = words.pop(1)
    print word
    
def sort_sentence(sentence):
    """takes in a full sentence adn returns the sorted words"""
    words = break_words(sentence)
    return sorted(words)
 
def print_first_and_last (sentence):
    """prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """sort the words of a sentence and print first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)       
    































