import tree as tr
import unittest

t=tr.Tree()
list_words =["test","command","cat","caterpillar","chown","chmod","chroot","table","words","word","word","word","wordd"]
for i in list_words :
  t.insert_word(i)

t.insert_word("words",100)

class TestTree(unittest.TestCase) :
  #def test_create_tree(self) :
    #self.failUnlessRaises(ValueError,tr.Tree)
      
  def test_count(self) :
    self.assertEqual(t.word_count("word"),3)
    
  def test_traverse_1(self) :
    self.assertItemsEqual(t.traverse("t"),{'test':1,'table':1}) 
    
  def test_traverse_2(self) :
    self.assertItemsEqual(t.traverse("c"),{'chown':1,'chmod':1,'chroot':1})
  
  def test_traverse_3(self) :
    self.assertItemsEqual(t.traverse("w"),{'word':3,'words':101,'wordd':1})  
    
  
  
  #def test_count(self) :
    #self.assertEqual(t.word)


#print "TEST 1 : ", t.word_count("word")

#print "TEST 2 : ", t.traverse("wu")

#print "TEST 3 : ", t.word_count("letra")



if __name__ == '__main__':
  unittest.main()

      