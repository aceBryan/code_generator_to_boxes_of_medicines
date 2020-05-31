"""
|================================================================================|
|This program returns random letters.                                            |
|================================================================================|
"""

from random import choice

def upper_letter_generator():
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    capital = capital_letters(upper_letters)
    return capital

def capital_letters(upper_letters):
    upper = choice(upper_letters)
    return upper

if __name__ == "__main__":
    upper_letter_generator()