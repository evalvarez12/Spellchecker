import tree as tr
import suggest as sg
import unittest

t=tr.Tree()
list_words =["test","command","cat","caterpillar","chown","chmod","chroot","table","words","word","word","word","wordd"]
for i in list_words :
  t.insert_word(i,2)

t.insert_word('chmod',1)
t.insert_word('chown',50)
t.insert_word('chroot',1)
t.insert_word_times('chroot',100)

print sg.options(t,'c')

#class TestTree(unittest.TestCase) :
  ##def test_create_tree(self) :
    ##self.failUnlessRaises(ValueError,tr.Tree)
      
  #def test_count(self) :
    #self.assertEqual(t.word_count("word"),3)
    
  #def test_traverse_1(self) :
    #self.assertItemsEqual(t.traverse("t"),['test1','table1']) 
    
  #def test_traverse_2(self) :
    #self.assertItemsEqual(t.traverse("ch"),['chown1','chmod1','chroot1'])
  
  #def test_traverse_3(self) :
    #self.assertItemsEqual(t.traverse("w"),['word3','words1','wordd1'])  
    
  
  
  ##def test_count(self) :
    ##self.assertEqual(t.word)


##print "TEST 1 : ", t.word_count("word")

##print "TEST 2 : ", t.traverse("wu")

##print "TEST 3 : ", t.word_count("letra")



#if __name__ == '__main__':
  #unittest.main()

      