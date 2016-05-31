'''
Created on May 24, 2016

@author: remy
'''
import MySQLdb as mdb
import sys


if __name__ == '__main__':
    pass

print('Hello')


try:
    con = mdb.connect('localhost', 'secondary', 'test623', 'testdb');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    
    print "Database version : %s " % ver
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()

# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="secondary",         # your username
#                      passwd="test623",  # your password
#                      db="testdb")        # name of the data base
# 
# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()
# 
# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")
# 
# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]
# 
# db.close()