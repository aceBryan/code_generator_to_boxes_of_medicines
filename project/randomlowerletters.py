"""
|================================================================================|
|This program returns random lower letters.                                      |
|================================================================================|
"""

from random import choice

def lower_letter_generator():
    lower_letters = ["a", "b","c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", 
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lower = lower_letter(lower_letters)
    return lower

def lower_letter(lower_letters):
    lowercase = choice(lower_letters)
    return lowercase

if __name__ == "__main__":
    lower_letter_generator()