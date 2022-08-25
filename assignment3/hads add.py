import random
small_number=1
big_number=100
counter=1

while True:
    computer_guess=random.randint(small_number,big_number)
    print('is your number',computer_guess,'?\n 1.yes\n 2.bigger\n 3.smaller')
    result=input()
    
    if result=='yes' or result=='1':
        print('bade',counter,'bar tonestam hads bezanam')
        print('horaaaaaaaaaaa!!!!!!!!!')
        break
    
    elif result=='bigger' or result=='2':
        
         small_number=computer_guess+1
    
    elif result=='smaller' or result=='3':
        
        big_number=computer_guess
     
    else:
        print('dadash drost bzn dige oskol nakon')
        counter-=1
    
    counter+=1