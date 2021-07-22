import sys
import traceback
import logging
import python_db


mysql_username = 'gwrenter' # please change to your username
mysql_password= 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    #res=python_db.Select('SELECT * FROM Game;')
    print("Table before")
    python_db.Select('SELECT * FROM Game;')
    '''res=res.split('\n')# split the header and data for printing
    print("<br/>"+ "Table Game before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")'''
    GameId = 'NULL'
    Rank1 = sys.argv[1]
    Rank2 = sys.argv[2]
    Location = sys.argv[3]
    Date = sys.argv[4]
    val = GameId + ",'" + Rank1 + "','" + Rank2 + "','" + Location + "','" + Date + "'"
    python_db.insert("Game",val)
    print()
    print()
    print("Table after")
    #res = python_db.Select('SELECT * FROM Game;')
    python_db.Select('SELECT * FROM Game;')
    '''res=res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>"+ "Table Game after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")'''
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
