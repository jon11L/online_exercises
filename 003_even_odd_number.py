# instruction : Write a python program that checks whether a given number is even or odd using an if-else statement.

def check_even_odd(num):
    ''' check a number and return if it is an even or odd number.'''
    if num % 2 == 0:
        return 'Even number'
    else:
        return 'Odd number'
    
number = int(input("please type in a number: "))
print(check_even_odd(number))
