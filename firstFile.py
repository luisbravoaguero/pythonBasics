import time

name, age, eaten = "luis", 30, False

print(name, str(age), str(eaten))

spongebob = patrick = sandy = squidward = 30

print(spongebob)
print(patrick)
print(sandy)
print(squidward)

country = "peru"

print(country.join(name))

num1 = 19
num2 = 38.6
num3 = "42"

num1 = float(num1)
num2 = int(num2)
num3 = float(num3)

print(num1)
print(num2)
print(num3)

# name = input("what is your name?: ")
# age = str(input("How old are you?: "))
# happy = input("Are you happy?: ")

# print(name+" is "+age+" and "+happy+ " happy.")

name = "Luis Bravo"

first_name = name[:4]
last_name = name[3:]
funky_name = name[0:9:3]
funky_name1 = name[0:9:-1]
print("first name: " + first_name)
print("last name: " + last_name)
print("last name: " + funky_name)
print("last name: " + funky_name1)

website = "http://www.google.com.pe"
slice = slice(11, -7)

print(website[slice])

condition = 'y'
while condition.lower() == 'y':
    age = int(input("How old are you?: "))
    if age == 100:
        print('You are a fucking legend')
    elif age > 100:
        print('You are a fucking fucking')
    elif age >= 18:
        print('You are a fucking adult')
    elif age < 0:
        print('What is wrong with you! fucking being human!')
    else:
        print('You are a fucking child')

    state = True
    condition = 'p'
    while state:
        if not (condition == 'y' or condition == 'n'):
            print("Write a valid input 'y' or 'n': ")
            condition = input('Would like to try again? Yes(Y) / No(N): ')
        else:
            state = False

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print('Welcome to a new country')

for index in "Luis Bravo":
    print(index)

# nested loop
# break continue pass
# lists

list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for index in list:
    print(index, end=" ")

for indexe in list:
    element = indexe
    print()
    #print(index, end=" ")
    print('---------------')
    for j in element:
        print(j)

state = True
iterator = 0
while state:
    if iterator < 5:
        print("iterator: "+str(iterator))
    else:
        state = False
    iterator += 1