from time import sleep
import random
p=[i for i in range(1,91)]
l=[]
for i in range(1,91):
    if(len(l)==90):
        print("Number completed please restart . . .")
    else:  
        j=random.choice(p)
        print(j)
        sleep(2)
        l.append(j)
        p.remove(j)
