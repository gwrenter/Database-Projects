import sys
import traceback
import logging
import python_db
import mysql.connector


mysql_username = 'gwrenter' # please change to your username
mysql_password= 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    Date = sys.argv[1]
    query = "SELECT DISTINCT (SELECT University_Name FROM Team WHERE TeamId = TeamOneId) AS Local,(SELECT Nickname FROM Team WHERE TeamId = TeamOneId) AS Nickname,(SELECT University_Name FROM Team WHERE TeamId = TeamTwoId) AS Visitor,(SELECT Nickname FROM Team WHERE TeamId = TeamTwoId) AS Nickname, Location, ScoreOne,ScoreTwo,(CASE WHEN ScoreOne > ScoreTwo THEN (SELECT University_Name FROM Team WHERE TeamId = TeamOneId) WHEN ScoreOne = ScoreTwo THEN 'Draw' ELSE (SELECT University_Name FROM Team WHERE TeamId = TeamTwoId) END) as Winner FROM Result r JOIN Game g ON g.GameId =  r.GameId JOIN Team t ON  t.TeamId = r.TeamOneId  OR  t.TeamId = r.TeamTwoId WHERE Date =" + "'" + Date + "';"
    python_db.Select(query)
    #res=res.split('\n')# split the header and data for printing
    #print("<br/>" + "<br/>")
    #print("<br/>"+ "All results from this date this season:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    #for i in range(len(res)-2):
    #    print(res[i+2]+"<br/>")
    python_db.close() # close db
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
