import tree as tr
import suggest as sg
import unittest

t=tr.Tree()
list_words =["test","command","cat","caterpillar","chown","chmod","chroot","table","words","word","word","word","wordd"]
for i in list_words :
  t.insert_word(i)

t.insert_word('chmod',1)
t.insert_word('chown',50)
t.insert_word('chroot',1)


print t.traverse('c')