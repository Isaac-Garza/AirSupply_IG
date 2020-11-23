import mysql.connector
from prettytable import PrettyTable
from prettytable import from_db_cursor

def createFunc(cursor):
    print("\nYou've Selected CREATE")
    print("Which Table would you like to INSERT into?")

    selection = selectTable(cursor)

    # insertValue = raw_input("(VENDOR_ID, VENDOR_NAME, ACCOUNT_PAYABLE_BY_TERM)\n")
    value = "1009, \'Iron-Plating\', 30, 1"
    sql = "INSERT INTO " + selection + " VALUES (" + value + ")"

    print(sql)
    
    cursor.execute(sql)

    myDatabase.commit()
    print(mycursor.rowcount, "record inserted.")

    # if selection == 'SALES_REP_IG':
        
    # elif selection == 'ORDER_IG':

    # elif selection == 'ORDER_LINES_IG':

    # elif selection == 'PRODUCT_IG':

    # else:
    
    
def readFunc(cursor):
    print("\nYou've Selected READ")
    print("What Tables would you like to Select?")

    selection = selectTable(cursor)

    cursor.execute("SELECT * FROM " + selection)

    mytable = from_db_cursor(mycursor)
    print("================" + selection + "================")
    print(mytable)


def updateFunc(cursor):
    print("You've Selected UPDATE")
    print("Which table would you like to UPDATE?")

    selection = selectTable(cursor)

    print("Which Record would you like UPDATE? (Select by Vendor_ID)")
    cursor.execute("SELECT * FROM " + selection)

    mytable = from_db_cursor(mycursor)
    print(mytable)

    vendorID = raw_input("Record: ") 
    newVendorName = "Iron Plating"
    newAPT = "15"
    mysql = "UPDATE " + selection + " SET VENDOR_NAME = '" + newVendorName + "', ACCOUNTS_PAYABLE_TERMS = " + newAPT +" WHERE VENDOR_ID = " + vendorID + ";"
    
    cursor.execute(mysql)
    myDatabase.commit()
    print(mycursor.rowcount, "record updated.")

def deleteFunc(cursor):
    print("You've Selected DELETE")
    print("Which Table would you like to DELETE from?")
    selection = selectTable(cursor)

    print("Which Record would you like DELETE? (Select by Vendor_ID)")
    cursor.execute("SELECT * FROM " + selection)

    mytable = from_db_cursor(mycursor)
    print(mytable)

    vendorID = raw_input("Record: ") 

    mysql = "DELETE FROM " + selection + " WHERE VENDOR_ID = " + vendorID + ";"

    cursor.execute(mysql)
    myDatabase.commit()

    print(mycursor.rowcount, "record updated.")


def callSelection():
    inputError = True
    while(inputError):
        userInput = raw_input("What would you like to do?: \n" +
                            "C: Create\n" + 
                            "R: Read\n" + 
                            "U: Update\n" + 
                            "D: Delete\n" +
                            "Input: ")

        userInput = userInput[0].upper()

        if userInput == 'C':
            createFunc(mycursor)
            inputError = False
        elif userInput == 'R':
            readFunc(mycursor)
            inputError = False
        elif userInput == 'U':
            updateFunc(mycursor)
            inputError = False
        elif userInput == 'D':
            deleteFunc(mycursor)
            inputError = False
        else:
            print("\nError! Please Try again!")

def selectTable(cursor):
    cursor.execute("SHOW TABLES")
    
    count = 1
    table = {}
    for (table_name,) in cursor:
            print(str(count) + ": " + table_name.upper())
            table[count] = table_name.upper()
            count+=1

    inputError = True
    while(inputError):
        userInput = raw_input("Input: ")
        
        try:
            userInput = int(userInput[0])
            selection = table[userInput]
            print(selection)
            inputError = False
        except:
            print("Error! Invalid Input")
    
    return selection






myDatabase = mysql.connector.connect(
    host="localhost",
    database="airsupplydata2020",
    user="root",
    password="A8AfIcIsI!")

print("Welcome to the AirSupply Database! Please login:")
username = str(raw_input("Username: "))
password = str(raw_input("Password: "))

mycursor = myDatabase.cursor()
sql = "SELECT * FROM login_ig WHERE username = '" + username + "'"
mycursor.execute(sql)

result = mycursor.fetchall()

if (username == str(result[0][0]) and password == str(result[0][1])):
    choice = 'Y'
    while choice == 'Y':
        callSelection()
        choice = raw_input("Want to make another selection? (Y/N)\nChoice: ")
        choice = choice[0].upper()
else:
    print("ERROR!!!")





