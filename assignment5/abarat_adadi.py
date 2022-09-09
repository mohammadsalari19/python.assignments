
text = input('abart ra vared konid : ')
amalgar = ['*','/','+','-']
list_amalgar = []
counter = 0

for letter in text :
    
    for i in range(4):
        
        if letter == amalgar[i]:
            
            list_amalgar.append(letter)
            


for i in range(4):
    
    list_abarat = text.split(amalgar[i])
    text = ' '.join(list_abarat)
    
list_abarat = text . split(' ')

while ''in list_abarat :
    
    list_abarat.remove('')
    
    

for i in range(len(list_abarat)):
    
    list_abarat[i] = int (list_abarat[i])
    

while '*' in list_amalgar  or  '/' in list_amalgar:
    
    if list_amalgar[counter] == '*':
        
        list_abarat[counter] = list_abarat[counter] * list_abarat[counter+1]
        
        list_abarat.pop(counter+1) 
        list_amalgar.pop(counter)
        
        counter -= 1
        
    
    elif list_amalgar[counter] == '/':
        
        list_abarat[counter] = list_abarat[counter]/list_abarat[counter+1]
        
        list_abarat.pop(counter+1) 
        list_amalgar.pop(counter)

        counter -= 1
   
    
        
    counter += 1
    
    
    
counter = 0 
    
while '+' in list_amalgar  or  '-' in list_amalgar:   
        
    if list_amalgar[counter] == '+':
        
        list_abarat[counter] = list_abarat[counter]+list_abarat[counter+1]
        
        list_abarat.pop(counter+1) 
        list_amalgar.pop(counter)
        
        counter -= 1
        
    
    elif list_amalgar[counter] == '-':
        
        list_abarat[counter] = list_abarat[counter]-list_abarat[counter+1]
        
        list_abarat.pop(counter+1) 
        list_amalgar.pop(counter)

        counter -= 1
   
    
        
    counter += 1 
    
    
        
print('hasel abarat barabar ast ba : ',list_abarat[0])
    
