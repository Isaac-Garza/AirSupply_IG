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

def deleteFunc(cursor):
    print("You've Selected DELETE")

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

mycursor = myDatabase.cursor()

mycursor.execute("SELECT * FROM ORDER_IG")

mytable = from_db_cursor(mycursor)

print("==============================AirSupply Order==============================")
print(mytable)

choice = 'Y'
while choice == 'Y':
    callSelection()
    choice = raw_input("Want to make another selection? (Y/N)")
    choice = choice[0].upper()





