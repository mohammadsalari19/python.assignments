
tedad=int(input('che tedad nafar daird : '))
list_afrad=[]
counter=1

for i in range(tedad):
    print('asm nafar',counter,'ra vared konid : ',end='')
    asm=input()
    list_afrad.append(asm)
    counter+=1
    
    
for c in range(len(list_afrad)):
    shomarande=1
    
    for j in range(len(list_afrad)-1):

        if list_afrad[j]==list_afrad[j+1]:
            shomarande+=1
            
            
    if list_afrad!=[]:
        
       asm=list_afrad[0]
       print('tedad asm',"'",asm,"'",'dar list',shomarande,'add')
       
       while asm in list_afrad:
          list_afrad.remove(asm)
    