number=int(input('add sahih ra vared konid : '))
counter=0
invers=0
number_1=number
while number!=0:
    invers=(number%10)+(invers*10)
    number=number//10
print('makos add',number_1,'mosavi ast ba :',invers,sep='')
if number==invers:
    print('pas add ',number_1 ,'ba makosash barabar ast')
else:
     print('pas add ',number_1 ,'ba makosash barabar nist')





