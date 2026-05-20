import random

cub =[1,2,3,4,5,6]
double=0
chifrePair=0
doubleOuPair=0
for i in range(100):
    cub1 = random.choice(cub)
    cub2 = random.choice(cub)
    if cub1 == cub2:
        double += 1
    if cub1 % 2 == 0 and cub2 % 2 == 0:
        chifrePair += 1
    if cub1 == cub2 or (cub1 % 2 == 0 ):
        doubleOuPair += 1
print("prob de double est : ", double/100)
print("prob de chifre pair est : ", chifrePair/100)
print("prob de double ou chifre pair est : ", doubleOuPair/100)