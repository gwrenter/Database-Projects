import sys
import traceback
import logging
import python_db


mysql_username = 'gwrenter'  # please change to your username
mysql_password = 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost', mysql_username,
                            mysql_password, mysql_username)  # open database
    query = """SELECT (CASE WHEN ScoreOne > ScoreTwo THEN(SELECT University_Name FROM Team WHERE TeamId=TeamOneId) WHEN ScoreOne < ScoreTwo THEN(SELECT University_Name FROM Team WHERE TeamId=TeamTwoId)
    END) AS Teams, COUNT(*) AS Victories FROM Result WHERE(CASE WHEN ScoreOne > ScoreTwo THEN(SELECT University_Name FROM Team WHERE TeamId=TeamOneId) WHEN ScoreOne < ScoreTwo THEN(SELECT University_Name FROM Team WHERE TeamId=TeamTwoId)
    END) IS NOT NULL GROUP BY Teams ORDER BY Victories DESC;"""
    python_db.Select(query)
    print("</br>")
    print("</br>")
    query2 = """SELECT (CASE WHEN ScoreOne > ScoreTwo THEN (SELECT University_Name FROM Team WHERE TeamId = TeamTwoId)
    WHEN ScoreOne < ScoreTwo THEN (SELECT University_Name FROM Team WHERE TeamId = TeamOneId) END) AS Teams,COUNT(*) AS Defeats
    FROM Result WHERE (CASE WHEN ScoreOne > ScoreTwo THEN (SELECT University_Name FROM Team WHERE TeamId = TeamTwoId)
    WHEN ScoreOne < ScoreTwo THEN (SELECT University_Name FROM Team WHERE TeamId = TeamOneId) END) IS NOT NULL
    GROUP BY Teams
    ORDER BY Defeats DESC;"""
    python_db.Select(query2)
    python_db.close()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
