import sqlite3 as lite
import sys
import tree as tr


def dump(t,db_name) :
  con=lite.connect(db_name)
  with con  :
    cur = con.cursor() 
    a=t.traverse('')
    cur.execute("DROP TABLE if exists root")
    cur.execute("CREATE TABLE root(word TEXT, times INT)")
    for k,v in a.iteritems() :
      s="INSERT INTO Root VALUES(" + "'" + k + "'"  + "," + str(v) + ")"
      cur.execute(s)


def load(t,db_name) :
  con=lite.connect(db_name)
  with con :
    cur = con.cursor() 
    s="SELECT * FROM root"
    cur.execute(s)
    items = cur.fetchall()
    for i in items :
      t.insert_word(str(i[0]),i[1])
    
