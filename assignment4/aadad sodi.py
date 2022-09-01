list_karbar=[]
list_addad=[]
counter=1

for j in range(10):
    print('add',counter,'ra vared konid :',end='')
    add=float(input())
    list_karbar.append(add)
    counter+=1
  
    
counter=0
while counter<10:
    
   add=list_karbar[0]
   for i in range (len (list_karbar)-1):
       
     if add>=list_karbar[i+1]:
         
         add=list_karbar[i+1]
         
        
   list_addad.append(add)
   list_karbar.remove(add)
   counter+=1
   
 
print('aadd b sorat sodi :')  
print(list_addad)