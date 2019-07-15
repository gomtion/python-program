'''def is_even(number):
    return number % 2 == 0
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_even,numbers)))


numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(lambda x : x % 2 == 1,numbers)))

from functools import *

def fold(words):
    i=0
    z = ""
    while(i < len(words)):
        z = z + words[i]
        i = i + 1
        
    print(z)
     
fold(["hello" , "world"])'''
    
 # printing out a list of positive numbers from this list(numbers)   
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positives = [n for n in numbers if n < 0]
print(positives)

# print out a list of even numbers from this list(numbers)
numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


