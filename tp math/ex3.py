import math 
import random
tre=0
gan = ""
while (tre < 6) :
    a =random.randint(1,6)
    if a ==6 :
        gan="liv"
        break
    else:
      tre +=1
if gan=="" :
  print("le tortue ganie : ")
else :
  print("le   lapin ganie")