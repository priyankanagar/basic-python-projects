

import random


while True:

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    print(d1)
    print(d2)
    print("The sum of the dice is ", (d1+d2))

    if d1 == d2:
        print("Doubles! Roll again!")

    input("Press enter to roll again")
