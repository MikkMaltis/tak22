import random
n = random.randrange (1,100)
guess = int(input("Sisesta number (1-100) "))
while n!= guess:
    if guess < n:
        print ("Liiga väike")
        guess = int(input("Sisesta uuesti number (1-100) "))
    elif guess > n:
        print ("Liiga suur")
        guess = int(input("Sisesta uuesti number (1-100) "))
    else:
        break
print ("Õige number")