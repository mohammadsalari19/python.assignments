temperature_conversion_type=(input('1.celsius to fahrenheit or c>f\n2.fahrenheit to celsius or f>c\n3.kelvin to fahrenheit or k>f\n4.fahrenheit to kelvin or f>k\n5.kelvin t celsius or k>c\n6.celsius to kelvin or c>k\nenter number for conversion or type '))

counter=1
while counter<3:

    if(temperature_conversion_type=='1' or temperature_conversion_type=='c>f'):
        celsius=float(input('enter the temperature in celsius: '))
        fahrenheit=(celsius*9/5)+32
        print('temperature in fahrenheit is:',fahrenheit)
        counter=5

    elif(temperature_conversion_type=='2' or temperature_conversion_type=='f>c'):
        fahrenheit=float(input('enter the temperature in fahrenheit: '))
        celsius=(fahrenheit-32)*5/9
        print('temperature in celsius is:',celsius)
        counter=5
    elif(temperature_conversion_type=='3' or temperature_conversion_type=='k>f'):
        kelvin=float(input('enter the temperature in kelvin: '))
        fahrenheit=(kelvin*9/5)-459.67
        print('temperature in fahrenheit is:',fahrenheit)
        counter=5
    elif(temperature_conversion_type=='4' or temperature_conversion_type=='f>k'):
        fahrenheit=float(input('enter the temperature in fahrenheit: '))
        kelvin=(fahrenheit+459.67)*5/9
        print('temperature in kelvin is:',kelvin)
        counter=5
    elif(temperature_conversion_type=='5' or temperature_conversion_type=='k>c'):
        kelvin=float(input('enter the temperature in kelvin: '))
        celsius=kelvin-273
        print('temperature in celsius is:',celsius)
        counter=5
    elif(temperature_conversion_type=='6' or temperature_conversion_type=='c>k'):
        celsius=float(input('enter the temperature in celsius: '))
        kelvin=celsius+273
        print('temperature in kelvin is:',kelvin)
        counter=5
    else:
     print('you entered the worng number or type')
     temperature_conversion_type=int(input('try again: '))
     counter=counter+1
     if(d==3):
        print('migam add bzn ya noee tabdil chikar mikoni ')
        
    
            
 

        
    
    

    


    



    
