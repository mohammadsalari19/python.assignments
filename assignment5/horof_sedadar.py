text = input ('abarat ra vared konid : ')

list_text = []
list_seda = ['i', 'o', 'u', 'e', 'a', 'I', 'O', 'U', 'E', 'A']

for letter in text :
    
    list_text.append(letter)
    
for i in range (len(list_text)):
    
    if list_text[i] in list_seda :
        
        list_text[i] = '?'
        
print(''.join(list_text))