
text = input('enter the word : ')

list_text = []
list_rtext = []


for letter in text :
    
    list_text .append(letter)

while  ' ' in list_text :
    
    list_text.remove(' ')

for i in range(len(list_text)):
    
    list_rtext.append(list_text[-i-1])

    
if list_text == list_rtext :
    
    print (' the word is palindorme')
    
else :
    
    print (' the word is not palindorme')
    
    
