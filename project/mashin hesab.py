number_of_uses=int(input('chand bar mikhahid estefade konid :'))
counter=1
sum=0
import math
basic_or_advance=input('az kodam ghsmat mashin hesab mikhahid estefade konid:\n1.basic\n2.advanced\n')
for i in range(number_of_uses) :
 if(basic_or_advance=='1' or basic_or_advance=='basic' ):
   print('az kodam amal gar estefade mikonid\n1.jam or +\n2.tafrigh or -\n3.zarb or *\n4.tahgsim or /\n5.taghsim sahih or //')
   print('6.mod or %/\n7.ghadr motlagh or ||\n8.tavan 2 or ^2 or **\n9.tavan or ^\n10.sin\n11.cos\n12.tan\n13.cotan')
   print('14.jzr or radical\n15.add aval')
   type_use=input()
   if(type_use=='+' or type_use=='jam' or type_use=='1' ):
     while True:
       num=(input('add ra vared konid dar payan "=" ra bezanid : '))
       if num=='=':
         print('hasel barbar ast ba :',sum)
         break
       number=float(num)
       sum+=number
   elif(type_use=='-' or type_use=='tafrigh' or type_use=='2'):
      while True:
        num2=input('add ra vared konid dar payan "=" ra bezanid :')
        if num2=='=':
          print('hasel barbar ast ba :',sum)
          break
        number2=float(num2)
        sum-=number2
   elif(type_use=='*' or type_use=='zarb' or type_use=='3'):
     sum=1
     while True:
        num3=input('add ra vared konid dar payan "=" ra bezanid :')
        if num3=='=':
          print('hasel barbar ast ba :',sum)
          break
        number3=float(num3)
        sum*=number3
   elif(type_use=='/' or type_use=='taghsim' or type_use=='4'):
      a=1
      while True:
       num=input('add ra vared konid dar payan "=" ra bezanid :')
       if num=='=':
         break
       number=float(num)
       if a==1:
          sum=number
          a=10
       else:
          if number==0:
           print('add taghsim bar 0 bi mobham ast add digari vared konid : ')
           continue
          else:
            sum=sum/number    
      print('hasel barbar ast ba :',sum)  
   elif(type_use=='//' or type_use=='taghsim sahih' or type_use=='5'):
     number5=int(input('add ra vared konid : '))
     number6=int(input('taghsim sahih bar che addi ast : '))
     if number6==0:
       print('add taghsim bar 0 mobaham ast ')
     else:
       sum4=number5//number6
       print('hasel taghsim sahih shod :',sum4)
   elif(type_use=='%' or type_use=='mod' or type_use=='6'):
     number7=int(input('add ra vared konid : '))
     number8=int(input('baghi mande taghsim bar che addi ast : '))
     if number8==0:
       print('add taghsim bar 0 mobaham ast ')
     else:
       sum5=number7%number8
       print('baghi mande taghsim sahih shod :',sum5) 
   elif(type_use=='||' or type_use=='ghadr motlagh'or type_use=='7'): 
      number9=float(input('add ra vared konid : '))
      print('ghadr motlagh add mosavi ast ba',abs(number9))             
   elif(type_use=='**' or type_use=='tavan 2' or type_use=='^2' or type_use=='8'):
     number10=float(input('add ra vaerd konid : '))
     sum10=number10**2
     print('hasel barbar ast ba:',sum10)    
   elif(type_use=='^' or type_use=='tavan' or type_use=='9'):
     number12=float(input('abtada add v sepas tavan ra vared konid : '))
     number11=float(input())
     if number12==0 and number11<0:
       print('add 0 b tavan add manfi mobaham ast')
     else:
       sum11=math.pow(number12,number11) 
       print('hasel barbar ast ba:',sum11)  
   elif type_use=='sin' or type_use=='10' :
     number13=float(input('sinos che addi ra mikhahid:'))
     while True:
       type1=input('add az kodam noe ast\n1.darage 2.radian')
       if type1=='2'or'radian':
          print('hasel barabar ast ba :',math.sin(number13))
          break
       elif type1=='1'or'darage':
         print('hasel barabar ast ba :',math.sin(math.radians((number13))))
         break
       else:
          print(' dobare sai konid')  
          continue                
   elif type_use=='cos' or type_use=='11' :
     number13=float(input('cosinos che addi ra mikhahid:'))
     while True:
        type1=input('add az kodam noe ast\n1.darage 2.radian')
        if type1=='2'or'radian':
          print('hasel barabar ast ba :',math.cos(number13))
          break
        elif type1=='1'or'darage':
          print('hasel barabar ast ba :',math.cos(math.radians(number13)))
          break
        else:
          print(' dobare sai konid')  
          continue                                                   
   elif type_use=='cot' or type_use=='13' :
     number13=float(input('cotanjhant che addi ra mikhahid:'))
     while True:
       type1=input('add az kodam noe ast\n1.darage 2.radian')
       if type1=='2'or'radian':
         print('hasel barabar ast ba :',1/math.tan(number13))
         break
       elif type1=='1'or'darage':
         print('hasel barabar ast ba :',1/math.tan(math.radians(number13)))
         break
       else:
         print(' dobare sai konid')  
         continue                     
   elif type_use=='tan' or type_use=='12' :
     number13=float(input('tanjhant che addi ra mikhahid:'))
     while True:
        type1=input('add az kodam noe ast\n1.darage 2.radian')
        if type1=='2'or'radian':
          print('hasel barabar ast ba :',math.tan(number13))
          break
        elif type1=='1'or'darage':
          print('hasel barabar ast ba :',math.tan(math.radians(number13)))
          break
        else:
          print(' dobare sai konid')  
          continue                                      
   elif type_use=='jzr' or type_use=='14 ':
     number15=float(input('add ra vared konid :')) 
     if number14>0:
        print('hasel barbar ast ba :',math.sqrt(number15))
     else:
       print('forge 2 aadade manfi mobham ast')             
   elif type_use=='add aval' or type_use=='15' :
       number14=int(input('add ra vared konid : '))                                  
       if 0<number14<10:
          if number14==4 or 6 or 8 or 9:
           print('add aval nis')
          else :
           print('add aval ast')   
       elif number14%2==0 or number14%3==0 or number14%5==0 or number14%7==0:
          print('add aval nis')
       elif number14<=0:
          print('add moshakhs nis')
       else:
          print('add aval ast')  
    print('shoma', counter,'az mashin hesab estefade kardid')
    counter+=1
 elif( basic_or_advance=='2' or basic_or_advance=='advanse'):
   print('az kodam ghsmat estafade mikonid :\n1.asin\n2.acos\n3.atan\n4.log\n5.ln\n6.sinh\n7.cosh\n8.tanh')
   type_use=input()
   if type_use=='asin' or type_use=='1' :
     number=float(input('add ra vared konid : '))
     sum=math.asin(number)
     piadd=math.pi/sum
     print('hasel b sort radian barabar ast :',sum,'\tya \tpi/',piadd,sep='')        
     print('hasel b sort darage barabar ast :',math.degrees(sum) )
   elif type_use=='acos' or type_use=='2' :
     number=float(input('add ra vared konid : '))
     sum=math.acos(number)
     piadd=math.pi/sum
     print('hasel b sort radian barabar ast :',sum,'\tya \tpi/',piadd,sep='')        
     print('hasel b sort darage barabar ast :',math.degrees(sum) )
   elif type_use=='atan' or type_use=='3' :
     number=float(input('add ra vared konid : '))
     sum=math.atan(number)
     piadd=math.pi/sum
     print('hasel b sort radian barabar ast :',sum,'\tya \tpi/',piadd,sep='')        
     print('hasel b sort darage barabar ast :',math.degrees(sum) )
   elif type_use=='log' or type_use=='4' :
     number=float(input('add ra vared konid : ')) 
     number2=int(input('log da che mabnaii ast: ')) 
     if number2==0:
       print('add dar banai 0 mobham ast')   
     sum=math.log(number,number2)
     print('log',number,'dar mbnai',number2,'  = ',sum)
   elif type_use=='ln' or type_use=='5' :
     number=float(input('add ra vared konid : '))
     sum=math.log(number,math.e) 
     print('log',number,'dar mbnai e  =',sum)
   elif type_use=='sinh' or type_use=='6' :
     number=float(input('add ra vared konid : '))
     sum=math.sinh(number)      
     print('hasel barabar ast :',sum)       
   elif type_use=='cosh' or type_use=='7' :
     number=float(input('add ra vared konid : '))
     sum=math.cosh(number)      
     print('hasel barabar ast :',sum)  
   elif type_use=='tanh' or type_use=='8' :
     number=float(input('add ra vared konid : '))
     sum=math.tanh(number)      
     print('hasel barabar ast :',sum)   
   print('shoma', counter,'az mashin hesab estefade kardid')          
   counter+=1
