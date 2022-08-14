print('bmi da groh hay mokhtalf seni v faliyat hay varzeshim mokhtalf motefavet ast\ndar in barname b sorat aam bmi mohasebe mishvad\n')
weight=float(input('vazn ra bar hasb kilogram vared konid: '))
height=float(input('ghad ra bar hasb metr vared konid bray ;mesal 180cm=1.8m: '))
bmi=(weight)/(height**2)
kodak=input('agr fard zir 18 sal  darad "y"  dar ghir in sorat kalame digar ra bezanid: ')
if(kodak=='y'):
    jensiyat=input('agr fard psar ast "p" agr dokhtar ast "d"ra bzanid : ')
    if(jensiyat=='p'):
        if(bmi<18.2):
            print('bmi shoma',bmi,' haaghl bmi monaseb 18.2 ast\nmoraghb kambod vazn bashid!!!!!')
        elif(26>bmi>=18.2):
            print('bmi shoma',bmi,' 26>bmi>18.2 monasb ast\n vazn shma monaseb ast agr dar noghat marzi hastid moraghb bashid!')
        elif(30>bmi>=26):
            print('bmi shoma',bmi,' hadaksar bmi monasb 26 ast\nmoraghb azafe vazn khod bashid!!!')
        else:
            print('bmi shoma',bmi,'hadaksar bmi monasb 26 ast\nvazn khod ra kahesh dahid')
    elif(jensiyat=='d'):
          if(bmi<17.4):
            print('bmi shoma',bmi,' haaghl bmi monaseb 18.2 ast\nmoraghb kambod vazn bashid!!!!!')
          elif(26.2>bmi>=17.4):
            print('bmi shoma',bmi,' 26.2>bmi>17.4 monasb ast\nvazn shoma mnaseb ast agr dar noghat marzi hastid moraghb bashid!')
          elif(28>bmi>=26.2):
            print('bmi shoma',bmi,' hadaksar bmi monasb 26.2 ast\nmoraghb azafe vazn khod bashid!!!')
          else:
            print('bmi shoma:',bmi,' hadaksar bmi monasb 26.2 ast\nvazn khod ra kahesh dahid')
    else:
        print('kalme eshtebah vared shod')
else:
    if(bmi<18.5):
            print('bmi shoma',bmi,' haaghl bmi monaseb 18.5 ast\nmoraghb kambod vazn bashid!!!!!')
    elif(24.9>bmi>=18.5):
            print('bmi shoma',bmi,' 18.5>bmi>24.9 monasb ast\nvazn shoma mnaseb ast agr dar noghat marzi hastid moraghb bashid!')
    elif(29.9>bmi>=24.9):
            print('bmi shoma',bmi,' hadaksar bmi monasb 24.9 ast\n shoma azafe vazn darid\nmoraghb azafe vazn khod bashid!!!')
    elif(34.9>bmi>=29.9):
            print('bmi shoma:',bmi,' hadaksar bmi monasb 24.9 ast\n vazn khod ra kahesh dahid')
    else:
         print('bmi shoma:',bmi,' hadaksar bmi monasb 24.9 ast\n ba dashtan rezhim monasb v moraje b pezshk har ch sare tar vazn khod ra kahesh dahaid khahshan')

          
print('       \n\n  ba aezoye salamati brai shmoa \n\n       ')