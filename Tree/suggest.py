import tree as tr

def options(t,word) :
  a=t.traverse(word)
  frecs=a.values()
  commands=a.keys()
  frecs,commands = (list(t) for t in zip(*sorted(zip(frecs,commands),reverse=True)))
  return [commands[i] for i in range(len(commands)) if i < 3]    

    

#a=t.traverse(word)
#frecs=[]
#commands=[]
#for i in a:
  #commands+=[i[:-1]]
  #frecs+=[int(i[-1])]
#frecs,commands = (list(t) for t in zip(*sorted(zip(frecs,commands),reverse=True)))
#res= [commands[i] for i in range(len(commands)) if i < 3]    