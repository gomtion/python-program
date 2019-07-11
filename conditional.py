import datetime import date

def birth_year(year):
    today = date.today().year
    age = today - year
    print(f"you are {age} years old")

year = int(input("what is your year of birth? "))

birth_year(year)
