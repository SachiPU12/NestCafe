import sqlite3
import funcNextCafe

class Coffee():
    # program heading
    print("\n***************************************************\n*****~~~~~~ Welcome to the NestCafe...! ~~~~~~*****\n***************************************************")

# user inputs
class firstMethod(Coffee):
    for i in range(1, 50):
        # main program advice
        print("\nThis is starting point. Enter the related number of your selection : \n\t1.Buy a coffee\n\t2.Add a coffee\n\t3.Update a coffee\n\t4.Delete a coffee\n\t5.Get the machine details\n\t6.Exit")
        x = int(input("\nYour starting point number is : "))
        if (x == 1):
            funcNextCafe.buyCoffee()
        elif (x == 2):
            funcNextCafe.addCoffee()
        elif (x == 3):
            funcNextCafe.updateCoffee()
        elif (x == 4):
            funcNextCafe.deleteCoffee()
        elif (x == 5):
            funcNextCafe.machineDetails()
        elif (x == 6):
            print("Thank You. Come again.")
            break
        else:
            funcNextCafe.error()

if __name__  == '__main__':
    firstMethod()
