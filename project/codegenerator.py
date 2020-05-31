from randomupperletters import upper_letter_generator
from numbergenerator import number_generator
from randomlowerletters import lower_letter_generator

LENGTH = 10

def code_generator():
    text = ""
    text += upper_letter_generator()
    
    for number in range (LENGTH):
        text += str(number_generator())
    
    text += lower_letter_generator()
    
    return text

if __name__ == "__main__":
    code_generator()