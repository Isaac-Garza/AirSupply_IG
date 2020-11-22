import mysql.connector
from prettytable import PrettyTable
from prettytable import from_db_cursor

def createFunc(cursor):
    print("You've Selected CREATE")
    Helloworld
    
    
def readFunc(cursor):
    print("\nYou've Selected READ")
    print("What Tables would you like to Select?")

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

choice = ''
while choice == 'Y':
    callSelection()
    choice = raw_input("Want to make another selection? (Y/N)")
    choice = choice[0].upper()





