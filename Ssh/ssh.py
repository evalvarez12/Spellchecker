import paramiko, sys, os, socket

global host,username,line,input_file

line ="\n-------------------------------------------------------------------"








#try :
  #host = raw_input("Enter Host Address: ")
  #username = raw_input("Enter SSH username: ")
  
  
#except KeyboardInterrupt  :
  #print "\n\n User interrupted"
  #sys.exit(3)
  
  
  
  
def ssh_connect(host,username,password,port) :
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try :
    ssh.connect(host,port=port,username = username,password=password)
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print type(stdin)
    print stdout.readlines()
  except socket.error, e :
    print "Connection error ", e
    
  #ssh.close()
  


with open("host.txt","r") as host_file :
  data=host_file.read()
  host, port, password = data.split('\n')
  username, host = host.split('@')
  
  ssh_connect(host,username,password,int(port))
  
  