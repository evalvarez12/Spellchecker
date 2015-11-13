import sqlite3 as lite
import sys
import tree as tr


def dump(t,db_name) :
  try :
    con=lite.connect(db_name)
    cur = con.cursor() 
    a=t.traverse('')
    print " A: ", a
    cur.execute("CREATE TABLE if not exists Root(word TEXT, times INT)")
    cur.execute("INSERT INTO Root VALUES('pene',223)")
    for k,v in a.iteritems() :
      s="INSERT INTO Root VALUES(" + "'" + k + "'"  + "," + str(v) + ")"
      cur.execute(s)
    
  except lite.Error, e :  
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
  #finally:
    #if con:
        #con.close()
    
    

def load(t,db_name) :
  try :
    con=lite.connect(db_name)
    cur = con.cursor() 
    for k,v in a.iteritems() :
      s="SELECT * FROM root"
      cur.execute(s)
      items = cur.fetchall()
      print items
    
  except lite.Error, e :  
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
  finally:
    if con:
        con.close()
    

