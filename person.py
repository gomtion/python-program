def get_age(age):
    if(age < 40):
        print("you are not elegible")
        print(f"you are {age} years old")

    else:
        print("you are elegible")
        print(f"you are {age} years old")

def get_name(name):
    if(len(name) < 4 ):
        print("Name should be at lest 5 characters long")
    else:
        print(f"your name is {name}")


age = int(input("what is your age? "))
name = input("what is your name? ")


get_age(age)
get_name(name)




