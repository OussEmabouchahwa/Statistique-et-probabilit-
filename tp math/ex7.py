import random
import itertools
blanch =['b'+str(i) for i in range(1, 5)]
noires = ['n'+str(i) for i in range(1, 6)]
urne = blanch + noires
nbfavorable = 0
nbNoires = 0
tirages = list(itertools.combinations(urne, 3))
print("nombre de tirages : ", len(tirages))
for i  in  tirages :
    for indice in i :
        test = True
        if indice[0] != 'b' :
            test = False

            break
    if test == True :
        nbfavorable += 1


print("prob de blanch  : ", nbfavorable/len(tirages))

#2 
nbdifernt = 0 
for i  in  tirages :
       couler=[j[0] for j in i]
       if len(set(couler)) >1 :
        nbdifernt += 1

print("prob de 3 boules differentes : ", nbdifernt/len(tirages))
print(nbdifernt)
# 3 
nbblancplus  = 0 
for i  in  tirages :
      Couleurs = [j[0] for j in i]
      if Couleurs.count('b') > 1 :
     
        nbblancplus += 1

print("prob de blanc plus : ", nbblancplus/len(tirages))
print(nbblancplus)

# 4 
nbboulepaire =0 
for i in tirages :
    for indice in i :
        test = True
        num = indice[1:]
        if int(num) % 2 == 0 :
            test = False
            break
    if test == True :
        print(i)
        nbboulepaire += 1
print("prob de boule paire : ", nbboulepaire/len(tirages))
print(nbboulepaire)
           