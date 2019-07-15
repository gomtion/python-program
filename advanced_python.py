"""def is_even(number):
    return number % 2 == 0
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_even,numbers)))"""


"""numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(lambda x : x % 2 == 1,numbers)))"""

from functools import *

def fold(words):
    i=0
    z = ""
    while(i < len(words)):
        z = z + words[i]
        i = i + 1
        
    print(z)
     
fold(["hello" , "world"])
    