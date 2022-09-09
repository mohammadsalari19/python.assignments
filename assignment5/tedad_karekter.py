

text = input('enter the sentence : ')
number_letter = 0
number_word = 0
counter = 0

for letter in text:
    
    if  ('a' <= letter <= 'z')  or  ('A' <= letter <= 'Z'):
        
        number_letter += 1
        counter    += 1
        
        if counter == 2:
            
            number_word+=1
            
        continue
    
    else:
        
        counter = 0

number_character = len (text)   

number_enter_space = text.count('\n') + text.count(' ')

number_point_comma = text.count(',') + text.count('.')
    
print('number_character =',number_character,'\nnumber_letter =',number_letter,'\nnumber_word =',number_word)
print('number_enter_space =',number_enter_space,'\nnumber_point_comma',number_point_comma)