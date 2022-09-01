
import random
from typing import Counter
list_aadad=[]
tol_list = int( input ('tol list chnd add bashad : ') )
add = random.randint (0,100)
 
list_aadad.append(add)
counter=1

while counter < tol_list :
    
   add=random.randint(0,100) 
   
   if add  in  list_aadad:
       
       counter-= 1
       
       continue
   else:
       
       list_aadad.append(add)
       
   counter+=1
       
   
print(list_aadad)

