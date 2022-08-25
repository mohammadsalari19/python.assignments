ramz=[1,2,3,4]
khtar=[4,3,2,1]
ramz_karbar=[]
counter=0
while counter<3:
    
    ramz_karbar1=int(input('ramz ra vared konid : '))
    
    if ramz_karbar1//10000==0 and ramz_karbar1//1000!=0:
        
        for j in range(4):
            
            add=ramz_karbar1%10
            ramz_karbar.append(add)
            ramz_karbar1=ramz_karbar1//10
    
        if ramz_karbar==khtar:
            
            print('vared shavid') 
            break
            
        elif  ramz_karbar==ramz:
            
            print('lotfan montazer bemanid dastgah dar hal apdyt ast')#zang polis
            break
        
        else:
            
           if counter==2:
               print('hesab ghofl shod ') 
               
           else:
                print('ramz ashteah ast dobare talash konid') 
                counter+=1
                
                
    else:
        print('tedad addad ramz eshtbah ast do bare talash konid')
        counter-=1

            

    
    