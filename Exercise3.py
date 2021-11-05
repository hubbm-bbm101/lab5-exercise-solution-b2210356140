import random
x = random.randint(1,100)
y= int(input("I picked a number, guess which one!"))
while x != y:
    if y==x:
        break
    elif y<x:
        y= int(input("increase your number"))
    else:
        y= int(input("decrease your number"))
print("well done, i picked "+ str(x))
