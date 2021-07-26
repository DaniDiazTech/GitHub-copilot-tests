# Palindrome: a word, phrase, or sequence that reads the same backwards as forwards
def is_palindrome(word):
    """Returns true if the word is a palindrome."""
    return word == word[::-1]