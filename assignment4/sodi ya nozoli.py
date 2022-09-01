
counter_small=1
counter_big=1
list_aadad=[]

for i in range(10):
    
    number = float (input('entr numbers : '))
    
    list_aadad.append(number)
    
    
for j in range(9):
    
    if   list_aadad[j] > list_aadad[j+1] :
        
        counter_big+=1
        continue
        
    elif list_aadad[j] < list_aadad[j+1] :
        
        counter_small+=1
        continue
    
    else :
        break
    

if counter_big==10 or counter_small==10 :
    
    print ('yesssssssssss')
    
else:
    
    print ('nooooooo')