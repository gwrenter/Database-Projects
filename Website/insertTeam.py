import sys
import traceback
import logging
import python_db
import mysql.connector


mysql_username = 'gwrenter' # please change to your username
mysql_password= 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    #res =python_db.executeSelect('SELECT * FROM Team;')
    #res=res.split('\n')# split the header and data for printing
    #print("<br/>"+ "Table Team before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    #for i in range(len(res)-2):
    #    print(res[i+2]+"<br/>")
    TeamId = 'NULL'
    University_Name = sys.argv[1]
    Nickname = sys.argv[2]
    Rank = sys.argv[3]
    val = TeamId + ",'" + University_Name + "','" + Nickname + "','" + Rank + "'"
    python_db.insert("Team",val)
    #res = python_db.executeSelect('SELECT * FROM Team;')
    #res=res.split('\n')# split the header and data for printing
    #print("<br/>" + "<br/>")
    #print("<br/>"+ "Table Team after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    #for i in range(len(res)-2):
    #    print(res[i+2]+"<br/>")
    print("New team added successfully!")
    python_db.close() # close db
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
