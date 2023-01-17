import sqlite3
import dbNextCafe

dbNextCafe.db()

# connect with the NestCafe database
conn = sqlite3.connect('NestCafe.db')
cur = conn.cursor()

def buyCoffee():
    print("\nBuy a coffee activity is started...")
    print("Types of coffees with it's id numbers are : ")
    try:
        cur.execute("SELECT COFFEE_ID, TYPE FROM Coffee")
        row = cur.fetchall()
        for i in range(10):
            print(row[i])
            i += 1
    except:
            print()

    b = input("Enter your coffee id : ")
    try:
        cur.execute("SELECT COFFEE_ID, TYPE, PRICE, COUNTRY, FLAVOUR_CONTAIN, MATERIALS_PACKETS FROM Coffee WHERE COFFEE_ID=?", (b))
        row = cur.fetchone()

        print("Your can buy a coffee now. Your coffee details are : ")
        print("\tId :", row[0], "\tType :", row[1], "\n\tPrice : ", row[2], "\n\tCountry : ", row[3], "\n\tFlavour contain : ", row[4], "\n\tMaterials packets : ", row[5])

        c = int(input("\nEnter your money amount : "))
        if (c >= row[2]):
            cur.execute("INSERT INTO Sales(COFFEE_ID,TYPE,PRICE,MATERIALS_PACKETS) VALUES (?,?,?,?)", (row[0], row[1], row[2], row[5]))
            conn.commit()
            print("Sales history created successfully")

            d = int(c) - int(row[2])
            print("Your balance is : ", d)
        else:
            print("Money will be not enough")

    except:
        print("Your can't buy a coffee now.")

def addCoffee():
    print("\nAdd a coffee activity is started...\nYou can add a coffee now. Add your coffee details.")
    a = input("\tCoffee id : ")
    b = input("\tCoffee type : ")
    c = input("\tCoffee price : ")
    d = input("\tCoffee country : ")
    e = input("\tCoffee flavour contain : ")
    f = input("\tCoffee materials packets : ")
    try:
        cur.execute("INSERT INTO Coffee(COFFEE_ID,TYPE,PRICE,COUNTRY,FLAVOUR_CONTAIN,MATERIALS_PACKETS) VALUES (?,?,?,?,?,?)", (a, b, c, d, e, f))
        conn.commit()
        print("Record created successfully")
    except:
        print("Record created unsuccessfully. Please enter valid data")

def updateCoffee():
    print("\nUpdate a coffee activity is started...\nYou can update a coffee now. Update your coffee details.")
    a = input("\tCoffee id : ")
    b = input("\tCoffee type : ")
    c = input("\tCoffee price : ")
    d = input("\tCoffee country : ")
    e = input("\tCoffee flavour contain : ")
    f = input("\tCoffee materials packets : ")
    try:
        cur.execute("UPDATE Coffee SET TYPE='"+b+"',PRICE='"+c+"',COUNTRY='"+d+"',FLAVOUR_CONTAIN='"+e+"',MATERIALS_PACKETS='"+f+"' WHERE COFFEE_ID='"+a+"'")
        conn.commit()
        print("Record updated successfully")
    except:
        print("Record updated unsuccessfully. Please enter valid data")

def deleteCoffee():
    print("\nBuy a coffee activity is started...")
    a = input("Coffee id : ")
    try:
        cur.execute("DELETE FROM Coffee WHERE COFFEE_ID='"+a+"'")
        conn.commit()
        print("Record deleted successfully")
    except:
        print("Record deleted unsuccessfully. Please enter valid data")

def machineDetails():
    print("\nMachine details activity is started...")
    print("Enter the related number of your selection : \n\t1.Weight of coffee\n\t2.Weight of all coffees\n\t3.Value of all coffees brewed\n\t4.Total number of all coffees brewed\n\t5.Balance of row materials\n\t6.The number of coffee cups that can be made")
    y = int(input("\nYour number is : "))
    if(y == 1):
        try:
            print("\nTypes of coffees are : ")
            cur.execute("SELECT COFFEE_ID, TYPE, MATERIALS_PACKETS FROM Coffee")
            row = cur.fetchall()
            for i in range(20):
                print("\t",row[i])
                i += 1
        except:
            print()

        c = input("Enter your coffee id : ")
        try:
            cur.execute("SELECT COFFEE_ID, TYPE, MATERIALS_PACKETS FROM Coffee WHERE COFFEE_ID=?", (c))
            row = cur.fetchone()

            print("\tId :", row[0], "\n\tType :", row[1], "\n\tMaterials packets : ", row[2])
            print("\tWeight(gram) of coffee cup is : ",row[2]*5,"g")
        except:
            print()

    if (y == 2):
        try:
            cur.execute("SELECT SUM(MATERIALS_PACKETS * 5) FROM Sales")
            row = cur.fetchone()
            print("\tWeight(gram) of all coffee cups is : ", row ,"g")
        except:
            print()

    if (y == 3):
        try:
            cur.execute("SELECT SUM(PRICE) FROM Sales")
            row = cur.fetchone()
            print("\tValue of all coffees brewed is : Rs.", row)
        except:
            print()

    if (y == 4):
        try:
            cur.execute("SELECT COUNT(SALES_ID) FROM Sales")
            row = cur.fetchone()
            print("\tTotal number of all coffees brewed is : ", row)
        except:
            print()

    if (y == 5):
        try:
            cur.execute("SELECT SUM(MATERIALS_PACKETS) FROM Sales")
            row = cur.fetchone()

            print("\tBalance of row materials packets are : ",[20 - x for x in row])
        except:
            print()

    if (y == 6):
        print("\tThe number of coffee cups that can be made starting time...")
        try:
            cur.execute("SELECT TYPE FROM Coffee")
            row1 = cur.fetchall()

            cur.execute("SELECT MATERIALS_PACKETS FROM Coffee")
            row2 = cur.fetchall()

            for i in range(10):
                print("\t\t",row1[i]," : ",[20 / x for x in row2[i]])
                i += 1
        except:
            print()

        print("\tThe number of coffee cups that can be made now...")
        try:
            cur.execute("SELECT TYPE FROM Coffee")
            row1 = cur.fetchall()

            cur.execute("SELECT 20 - SUM(MATERIALS_PACKETS) FROM Sales")
            row2 = cur.fetchone()

            cur.execute("SELECT MATERIALS_PACKETS FROM Coffee")
            row3 = cur.fetchall()

            for i in range(10):
                print("\t\t",row1[i]," : ",[row2[0] / x for x in row3[i]])
                i += 1
        except:
            print()

def error():
    print("Not valid number. Please try again.")
