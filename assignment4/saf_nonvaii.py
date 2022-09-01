
saf_nonvaii = ['ali', 'atefe', 'reza', 'homa', 'amir', 'fateme']


for i in range(3):
    
    name_aghazade = input ('asm ton che agha zade jn : ')
    
    nafar_chnadom = int(input('nafar chandom saf mikhahid bashid : '))-1
    
    if nafar_chnadom == len(saf_nonvaii):
        
        print('damet garm',name_aghazade,'kash hame mesl to bodan jan del')
    
    saf_nonvaii.insert (nafar_chnadom , name_aghazade)   
    
print('nonva zod non bzn bache ha montazern inam az saf\n',saf_nonvaii) 
    