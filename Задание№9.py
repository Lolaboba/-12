#10 задача
from random import randint

qwq=[]
for i in range(10):
    qwq.append(randint(1,666))
asa = sum(qwq)/len(qwq)
print(asa)