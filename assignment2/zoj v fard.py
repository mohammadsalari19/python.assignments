add=int(input('add  ra vared konid:'))
fard=0
zoj=0
if(add<0):
    add=-1*add
else:
    add=add
while add>0 :
     if(add%2==0 or add==0):
            zoj=zoj+1
     else:
         fard=fard+1
     add=(add//10)

if(zoj>fard):
    print('tedad addad zoj bishtar ast')
elif(fard>zoj):
    print('tedad addad fard bishtar ast')
else:
    print('tedad adade zoj v fard brabar')