"""

Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
elvégzéséhez, és ezt is közölje a felhasználóval!

"""

# Getting the variables
d = float(input("How big is your melon? (m) "))
quantity = float(input("How much melons do you have? "))
tape = float(input("How much tape do you have? (m) "))
pi = 3.14

# Counting the required tape
n = needed_tape = round((d * pi * quantity) + 0.6, 2)

# Printing the output
if n > tape:
    print(f"You don't have enough tape! Tape required: {n} meters")
elif n < tape:
    print(f"You need {n} meters of tape to pack your melons! ")
else:
    print("Error")