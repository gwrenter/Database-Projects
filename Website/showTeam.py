import sys
import traceback
import logging
import python_db


mysql_username = 'gwrenter'  # please change to your username
mysql_password = 'reeK8mie'  # please change to your MySQL password

try:
    python_db.open_database('localhost', mysql_username,
                            mysql_password, mysql_username)  # open database
    res = python_db.Select('SELECT University_Name AS "University Name",Nickname,Rank FROM Team ORDER BY Rank ASC;')
    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close_db()  # close db

except Exception as e:
    logging.error(traceback.format_exc())
