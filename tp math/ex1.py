import random
nbf=0
nbg=0
files =['f'+str(i)+'.txt' for i in range(1, 11)]
garcon = ['g'+str(i) for i in range(1, 14)]
classes= files + garcon
id= random.choice(classes)
//ex2 
print("l'id de l'eleve est : ", id)
//ex3 
for in range (classes):
    if id in files:
        nbf+=1 
    else:
        nbg+=1

print ("le proba de avoir filles est : ", nbf /len(classes))
print ("le proba de avoir garcons est : ", nbg /len(classes))
