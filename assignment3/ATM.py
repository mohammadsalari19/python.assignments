ramz=[1,2,3,4]
khtar=[4,3,2,1]

counter=0
while counter<3:
    
    ramz_karbar1=int(input('ramz ra vared konid : '))
    ramz_karbar=[]  
     
    if ramz_karbar1//10000==0 and ramz_karbar1//1000!=0:
        
        for j in range(4):
            
          add=ramz_karbar1%10
          ramz_karbar.append(add)
          ramz_karbar1=ramz_karbar1//10
        
        if ramz_karbar==khtar:
            
            print('khos omadid ghasd anjam che amalyati darid ') 
            break
            
        elif  ramz_karbar==ramz:
            
            print('polic posht sarte dastato bzar ro saret dozd jn')
            break
        
        else:
            
           if counter==2:
               print('hesab ghofl shod ') 
               
           else:
                print('ramz ashteah ast ') 
                
                
    else:
        print('tedad addad ramz eshtbah ast do bare talash konid')
        counter-=1

    counter+=1         
