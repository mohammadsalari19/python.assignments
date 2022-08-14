loop=1
bord=0
bakht=0
mosavi=0
emtyaz=0
print('natije mosabegh ra b sorat zir  vard konid\n1. 1 or bord or win = bord\n2. 2 or mosavi or tie = mosavi\n3. 3 or bakht or lose = bakht ')

while loop<9 :
    print('natije mosabeghe',loop,'ra vard konid',end=':')
    natije=input()
    if( natije=='bo' or natije=='1' or natije=='win'):
        bord=bord+1
        emtyaz=emtyaz+3
    elif(  natije=='m' or natije=='2' or natije=='tie'):
        mosavi=mosavi+1
        emtyaz=emtyaz+1
    elif( natije=='ba' or natije=='3' or natije=='lose') :      
        bakht=bakht+1
    else:
        print('natije ra eshtebah vard kardid dobare sai konid')
        loop=loop-1
        
    loop=loop+1
print('emtyaz nahaii :',emtyaz,'\ntedad bord :',bord,'\ntedad mosavi :',mosavi,'\ntedad bakht :',bakht)






