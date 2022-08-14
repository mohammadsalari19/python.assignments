add=int(input('add ra vared konid : '))

if(add==0 or add%7!=0):
   print('add mazrab 7 nist')
   addbadi=int((add//7)*7+7)
   print('add badi mazrab 7 an barabar ast ba :',addbadi)
else:
    print('add',add,'mazrabi az 7 ast')
