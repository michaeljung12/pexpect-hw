#homework 1
newprimates = open ("primates2.nex", "w")
oldprimates = open ("primates.nex").read()
corrected = oldprimates.replace("mcmc","mcmp")
newprimates.write(corrected)
newprimates = open ("primates2.nex").read()
newprimates.find("mcmp")
newprimates = close ("primates2.nex")

#homework 1 continued
child = pexpect.spawn("mb -i primates2.nex")
#send the string "mcmc" to the process. This tells mrbayes to start running. The \r is carriage return
child.sendline(r"mcmcp") 
# tells mrbayes to stop the analysis (do not continue)
child.sendline("no")
# wait for the mrbayes prompt. 
child.expect("MrBayes >") 

print child.before
#now add a line to tell mrbayes to quit ("quit")
child.sendline("quit")

#homework 2
#spawn an interactive mrbayes process
child = pexpect.spawn("mb -i primates2.nex")
#send the command "execute primates2.nex" to mrbayes
child.sendline(r"execute primates2.nex")
#send the sumt command to mrbayes
child.sendline("sumt")
#check to see that the mrbayes command prompt is returned
child.expect("MrBayes >")
#print everything before the mrbayes prompt
print child.before
#send the sump command
child.sendline("sump")
#quit mrbayes
child.sendline("quit")

#homework 3
import pexpect
def child1fn (filename):
  #send the command "set nowarn = yes" to mrbayes
  child1 = pexpect.spawn("mb -i filename.nex")
  child1.sendline("set nowarn = yes")
  #send the command "mcmcp ngen = 1000" where XX is the string of numgen
  child1.sendline("mcmcp ngen = XX")
  #send the command "mcmc" to mrbayes
  child1.sendline(r"mcmc")
  #send the command "no" to mrbayes (do not continue analysis)
  child1.sendline("no") 
  #send the command "quit" to mrbayes
  child1.sendline("quit") 

def child2fn (filename):
  child2 = pexpect.spawn("mb -i " + filename + ".nex")
  child2.sendline(r"sump")
  child2.sendline(r"sumt")
  child2.sendline("quit")

import glob

