import sys
import traceback
import logging
import python_db
import mysql.connector

mysql_username = 'gwrenter' # please change to your username
mysql_password= 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    GameID = sys.argv[1]
    TeamOneId = sys.argv[2]
    TeamTwoId = sys.argv[3]
    ScoreOne = sys.argv[4]
    ScoreTwo = sys.argv[5]
    val = GameID + ",'" + TeamOneId + "','" + TeamTwoId + "','" + ScoreOne + "','" + ScoreTwo + "'"
    python_db.insert("Result",val)
    print("New result added successfully!")
    python_db.close() # close db
except mysql.connector.Error as err:
    print("Cannot add or update a child row. Please, first add a game to the Game table")



