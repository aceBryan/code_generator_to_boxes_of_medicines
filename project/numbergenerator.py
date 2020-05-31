from random import choice

def number_generator():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = picking_numbers(numbers)
    return num

def picking_numbers(numbers):
    number = choice(numbers)
    return number

if __name__ == "__main__":
    number_generator()