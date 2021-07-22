import sys
import traceback
import logging
import python_db


mysql_username = 'gwrenter' # please change to your username
mysql_password= 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    University_Name = sys.argv[1]
    query = "SELECT University_Name, Nickname,IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),(SELECT University_Name FROM Team WHERE TeamId = TeamTwoId),(SELECT University_Name FROM Team WHERE TeamOneId = TeamId)) AS Opponent,Date,IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo) AS 'University Score',IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo) AS 'Opponent Score',(CASE WHEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) > (IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) THEN (SELECT University_Name FROM Team WHERE University_Name =" + "'" + University_Name + "') WHEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) < (IF(TeamTwoId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'),ScoreOne,ScoreTwo)) THEN (IF(TeamOneId = (SELECT TeamId FROM Team WHERE University_Name =" + "'" + University_Name + "'), (SELECT University_Name FROM Team WHERE TeamId = TeamTwoId),(SELECT University_Name FROM Team WHERE TeamOneId = TeamId))) Else 'Draw' END) as Winner FROM Result r JOIN Game g ON g.GameId =  r.GameId JOIN Team t ON  t.TeamId = r.TeamOneId  OR  t.TeamId = r.TeamTwoId WHERE University_Name =" + "'" + University_Name + "'" + "ORDER BY g.GameId;"
    res = python_db.executeSelect(query)
    res=res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>"+ "All results from the University Team this season:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
