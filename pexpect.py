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
