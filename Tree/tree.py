

class Tree(object) :
  def __init__(self,trees=None) :
    self.trees = dict(trees) if trees else {}
    
  def insert_subtree(self, name, tree) :
    if name in self.trees :
      raise TreeAlreadyExists()
    
    self.trees[name] = tree
    
    
  def get(self, *args) :
    child_name, rest = args[0], args[1:]
    child = self._get_child(child_name)
    
    if len(rest) :
      return child.get(*rest)
    else :
      return [item for item in child]
    
  
  def _get_child(self, name) :
    if name not in self.trees:
      raise KeyError("Child %s does not exist" % name)
    return self.trees[name]

  def insert(self, *args):
    child_name, rest = args[0], args[1:]
    child = self._get_child(child_name)
    child.insert(*rest)

  def __iter__(self):
    for key in sorted(self.trees.keys()):
       for item in self.trees[key]:
         yield item

class TreeAlreadyExists(Exception):
    pass