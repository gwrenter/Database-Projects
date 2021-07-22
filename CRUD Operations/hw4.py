#-----------------------------------------------
#   CSCE 4523 Homework 4
#   Students: Gregory Renteria and Luis Pinzon
#   UAID: 010847790 and 010847033
#-----------------------------------------------

#--------------------------------------------------
# HOW TO USE THE PROGRAM?
# DO: more $HOME/.my.cnf to see your MySQL username
# and password.
# CHANGE: mysql_username and mysql_pwd in the main
# function to your username and mysql password
# RUN: python3 hw4.py
#--------------------------------------------------

import sys
import mysql.connector
from tabulate import tabulate


#--------------------
# Extra functions
#--------------------
def OpenDatabase(hostname,username,mysql_pwd,dbname):
    global conn
    conn = mysql.connector.connect(host = hostname, user = username,
                                   password = mysql_pwd, database = dbname)
    global cursor
    cursor = conn.cursor()


def CloseDatabase():
    cursor.close()
    conn.close()


def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    print(tabulate(result, headers=header))# print results in table format


def executeSelect(query):
    cursor.execute(query)
    printFormat(cursor.fetchall())


def executeUpdate(query):
    cursor.execute(query)
    conn.commit()


#--------------------------------------------------------
# Menu Option 1: SupplierCountry
# Find and list all available suppliers and coffee
# from that location.
# Display all information of those suppliers and coffees.
#--------------------------------------------------------
def SupplierCountry(country):
    query = "SELECT DISTINCT s.ID AS SUPPLIER_ID,s.Name AS SUPPLIER_NAME,PHONE_NUMBER,i.Name AS COFFEE_NAME,ROASTING FROM SUPPLIER s,ITEM i, INVENTORY_MGMT WHERE i.ID = ITEM_ID AND s.ID = SUPPLIER_ID AND ADDRESS = '" + country + "';"
    executeSelect(query)



def viewResult(University_Name):
    query = "SELECT University_Name, Nickname,IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),(SELECT University_Name FROM Team WHERE TeamId = TeamTwoId),(SELECT University_Name FROM Team WHERE TeamOneId = TeamId)) AS Opponent,Date,IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo) AS 'University Score',IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo) AS 'Opponent Score',(CASE WHEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) > (IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) THEN (SELECT University_Name FROM Team WHERE University_Name =" + "'" + University_Name + "') WHEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) < (IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) THEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'), (SELECT University_Name FROM Team WHERE TeamId = TeamTwoId),(SELECT University_Name FROM Team WHERE TeamOneId = TeamId))) Else 'Draw' END) as Winner FROM Result r JOIN Game g ON g.GameId =  r.GameId JOIN Team t ON  t.TeamId = r.TeamOneId  OR  t.TeamId = r.TeamTwoId WHERE University_Name =" + "'" + University_Name + "'" + "ORDER BY g.GameId;"
    executeSelect(query)





#------------------------------------------------------
# Menu Option 2: AddSupplier
# Prompts the user to enter a new supplier with name,
# phone number and country.
#------------------------------------------------------
def AddSupplier(supplier,phone_num,country,item):
    querySupplier = "INSERT INTO SUPPLIER(ID,NAME,PHONE_NUMBER,ADDRESS) SELECT(SELECT MAX(ID)+1 FROM SUPPLIER)," + "'" + supplier + "'" + "," + "'" + phone_num + "'" + "," + "'" + country + "'" + ";"
    executeUpdate(querySupplier)
    queryInventory = "INSERT INTO INVENTORY_MGMT VALUES((SELECT i.ID FROM ITEM i WHERE NAME = " + "'" + item + "'), (SELECT MAX(s.ID)FROM SUPPLIER s)," + "0,15);"
    executeUpdate(queryInventory)
    queryRecord = "SELECT ID,NAME,PHONE_NUMBER,ADDRESS FROM SUPPLIER WHERE PHONE_NUMBER= " + "'" + phone_num + "';"
    executeSelect(queryRecord)
    querySuppliers = "SELECT DISTINCT s.NAME AS COFFEE_SUPPLIERS FROM SUPPLIER s,ITEM i,INVENTORY_MGMT WHERE ITEM_ID = (SELECT it.ID FROM ITEM it WHERE NAME = " + "'" + item + "') AND s.ID = SUPPLIER_ID;"
    executeSelect(querySuppliers)


#------------------------------------------------------
# Menu Option 3: EmployeePerformance
# List all items sold by a specific employee.
#------------------------------------------------------
def EmployeePerformance(employee):
    query = "SELECT i.NAME AS ITEM_SOLD,ROASTING,COUNT(s.ITEM_ID) AS TOTAL_SALES FROM ITEM i,EMPLOYEE e,SALES s WHERE e.NAME = " + "'" + employee +"' AND e.ID = EMPLOYEE_ID AND i.ID = s.ITEM_ID GROUP BY i.NAME,ROASTING;"
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) == 0:
        print()
        print("No items sold by this employee")
    else:
        printFormat(result)


#-----------------------------------------------------
# Menu Option 4: UpdateItem
# Handles what happens when the company gets a new
# shipment or makes a sale.
#-----------------------------------------------------
def UpdateItem(item,choice):
    if choice == 1:
        shipment = input("Please enter the number of items shipped: ")
        updateShipment = "UPDATE INVENTORY_MGMT SET TOTAL_AVAILABLE = TOTAL_AVAILABLE + " + "'" + shipment + "' WHERE ITEM_ID = (SELECT ID FROM ITEM WHERE NAME = " + "'" + item + "');"
        executeUpdate(updateShipment)
        selectShipment = "SELECT NAME AS ITEM_NAME,TOTAL_AVAILABLE - " + "'" + shipment + "' AS TOTAL_AVAILABLE_BEFORE,TOTAL_AVAILABLE AS TOTAL_AVAILABLE_AFTER FROM ITEM,INVENTORY_MGMT WHERE ITEM_ID = (SELECT ID FROM ITEM WHERE NAME = " + "'" + item + "') AND NAME = " + "'" + item + "';"
        cursor.execute(selectShipment)
        resultShipment = cursor.fetchall()
        if len(resultShipment) == 0:
            print()
            print("This item does not exist in the inventory")
        else:
            printFormat(resultShipment)
    elif choice == 2:
        sale = input("Please enter the number of items sold: ")
        updateSale = "UPDATE INVENTORY_MGMT SET TOTAL_AVAILABLE = TOTAL_AVAILABLE - " + "'" + sale + "' WHERE ITEM_ID = (SELECT ID FROM ITEM WHERE NAME = " + "'" + item + "');"
        executeUpdate(updateSale)
        selectSale = "SELECT NAME AS ITEM_NAME,TOTAL_AVAILABLE + " + "'" + sale + "' AS TOTAL_AVAILABLE_BEFORE,TOTAL_AVAILABLE AS TOTAL_AVAILABLE_AFTER FROM ITEM,INVENTORY_MGMT WHERE ITEM_ID = (SELECT ID FROM ITEM WHERE NAME = " + "'" + item + "') AND NAME = " + "'" + item + "';"
        cursor.execute(selectSale)
        resultSale = cursor.fetchall()
        if len(resultSale) == 0:
            print()
            print("This item does not exist in the inventory")
        else:
            printFormat(resultSale)


#---------------------------------------------------
# Menu Option 5: Cancel Sales
# Handles ID transactions to cancel sales and the
# number of sales return back to the inventory.
#---------------------------------------------------
def CancelSales():
    transactionID = input("Please enter a transaction ID to cancel sales: ")
    # Query which updatate sales status to Cancelled
    queryCancel = ("UPDATE SALES SET status = 'CANCELLED' where TRANS_ID = " +
                   "'" + str(transactionID) + "'")
    executeUpdate(queryCancel)

    # Query which modifies the quantity in stock
    queryModified_Inventory = "UPDATE INVENTORY_MGMT m JOIN SALES s ON m.ITEM_ID=s.ITEM_ID SET m.TOTAL_AVAILABLE = m.TOTAL_AVAILABLE + s.Num_Items_sold WHERE TRANS_ID =" + \
        "'" + str(transactionID) + "'"
    executeUpdate(queryModified_Inventory)

    # Select of the items put back to stock
    modified_Inventory = "SELECT i.ITEM_ID, i.SUPPLIER_ID, i.TOTAL_ITEM_SALES_3_MONTHS, i.TOTAL_AVAILABLE FROM INVENTORY_MGMT i JOIN SALES s ON i.ITEM_ID=s.ITEM_ID WHERE s.TRANS_ID = " + "'" + str(transactionID) + "'"
    executeSelect(modified_Inventory)

    # Select of the modified sale
    modified_sale = "SELECT s.TRANS_ID, s.ITEM_ID, s.DISCOUNT, s.PURCHASE_DATE,s.EMPLOYEE_ID,s.status FROM SALES s WHERE TRANS_ID = " + "'" + str(transactionID) + "'"
    executeSelect(modified_sale)


def Menu():
    print()
    print("""Menu of Operations:
    1. Supplier by Country
    2. Add Supplier
    3. Employee Performance
    4. Update Item
    5. Cancel Sales
    6. Quit""")
    print()

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        country = input("Please enter the name of a country (ALL CAPS): ")
        SupplierCountry(country)
    elif choice == 2:
        supplier = input("Please enter a supplier name (ALL CAPS): ")
        phone_num = input("Please enter a phone number: ")
        country = input("Please enter the name of a country (ALL CAPS): ")
        item = input("Please enter a coffee item name the supplier provides: ")
        AddSupplier(supplier,phone_num,country,item)
    elif choice == 3:
        employee = input("Please enter an employee name (ALL CAPS): ")
        EmployeePerformance(employee)
    elif choice == 4:
        item = input("Please enter an item name (ALL CAPS): ")
        print("""Do you want to do?:
        1. Get a new shipment
        2. Make a sale""")
        choice = int(input("Please select an option: "))
        UpdateItem(item,choice)
    elif choice == 5:
        CancelSales()
    elif choice == 6:
        University_Name = input("Please enter an university name:")
        viewResult(University_Name)
    else:
        print("Goodbye!")
        CloseDatabase()
        sys.exit()


def Main():
    mysql_username = ''
    mysql_pwd = ''

    OpenDatabase('localhost',mysql_username,mysql_pwd,mysql_username)
    while True:
        Menu()

#The program initiates calling this function
Main()

