import sys

#class Node(object) :
  #def __init__(self,nodes=None) :
    #self.nodes = dict(nodes) if nodes else {}
    #self.numbers = {}


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

      self.trees[word[0]].insert_word(word[1:])
    else :
      print "motherfucker ", times
      self.number += times

  def insert_word_times(self,word,times) :
    if word :
      if word[0] not in self.trees :
        tree1 = Tree()
        self.trees[word[0]] = tree1

      self.trees[word[0]].insert_word(word[1:])
    else :
      print "motherfucker TIMES ", times
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
      #try :
      return [word[0] +  i for i in self.trees[word[0]].traverse(word[1:])]
      #except : 
        #print "Cant tranverse using " + word 
    else :
      if self.trees and self.number == 0:
	l=[]
      else :
	l= [str(self.number)]
      for k,v in self.trees.iteritems() :
	l+=[k + i for i in v.traverse(word)]
      return l      
      #return [k + i for i in  v.traverse(word)  for k,v in self.trees.iteritems()]
    
    
      

  #def insert_subtree(self, name, tree) :
    #if name in self.trees :
      #raise TreeAlreadyExists()
    
    #self.trees[name] = tree
    #self.numbers[name] = 1    
    
  #def get(self, *args) :
    #child_name, rest = args[0], args[1:]
    #child = self._get_child(child_name)
    
    #if len(rest) :
      #return child.get(*rest)
    #else :
      #return [item for item in child]
    
  
  #def _get_child(self, name) :
    #if name not in self.trees:
      #raise KeyError("Child %s does not exist" % name)
    #return self.trees[name]



  #def insert(self, *args):
    #child_name, rest = args[0], args[1:]
    #child = self._get_child(child_name)
    #child.insert(*rest)

  #def __iter__(self):
    #for key in sorted(self.trees.keys()):
      #for item in self.trees[key]:
	#yield item

#class TreeAlreadyExists(Exception):
    #pass