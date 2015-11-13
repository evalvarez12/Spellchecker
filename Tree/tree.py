import sys

class Tree(object) :
  def __init__(self) :
    #self.trees = dict(trees) if trees else {}
    self.trees = {}
    self.number = 0
    
  def insert_word(self,word,times=1) :
    if word :
      if word[0] not in self.trees :
        tree1 = Tree()
        self.trees[word[0]] = tree1

      self.trees[word[0]].insert_word(word[1:],times)
    else :
      self.number += times

  def word_count(self,word) :
    if word  :
      try :
        return self.trees[word[0]].word_count(word[1:])
      except :
	print "No word in tree " + word

    else :
      return self.number
      
  def traverse(self,word) :
    if word :
      try :
        return {(word[0]+k):v for k,v in self.trees[word[0]].traverse(word[1:]).iteritems()}
      except : 
        print "Cant tranverse using " + word 
    else :

      if self.number != 0  :
	l={'':self.number}
      else :
	l={}
      for k,v in self.trees.iteritems() :
	l.update({(k+i):j for i,j in v.traverse(word).iteritems()})

      return l   
    
  def fuzzy_traverse(self,word,err) :
    if word :
      try :
        return {(word[0]+k):v for k,v in self.trees[word[0]].traverse(word[1:]).iteritems()}
      except : 
        print "Cant tranverse using " + word 
    else :

      if self.number != 0  :
	l={'':self.number}
      else :
	l={}
      for k,v in self.trees.iteritems() :
	l.update({(k+i):j for i,j in v.traverse(word).iteritems()})

      return l 

    
      