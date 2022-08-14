from typing import Counter


username='mohammad'
pasword=12345
shomaresh=2
counter=0
while counter<3:
    k=input('user ra vard konid:')
    voroodi=int(input('pasword ra vared konid:'))

    if(k==username and voroodi==pasword):
        print('ejaze vord darid')
        counter=5

    else:
        print('mojaz b vorod nistid')
        if(shomaresh==0):
                print('tedad forsat shoma b payan resid v ekaknt ta 24 saat baste khoahad bood')
        else:
                print('shoma',shomaresh,'forsat digar darid ')
        shomaresh=shomaresh-1
        counter=counter+1
              

    

