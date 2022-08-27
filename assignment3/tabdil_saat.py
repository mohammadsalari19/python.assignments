hour_or_second=input('which one is the input\n1.hour \n2.second\n')

if (hour_or_second=='1' or hour_or_second=='hour'):
    
    time=input('inter the  time  as follows\n00:00:00 or 00-00-00 or 00 00 00')
    
    time_hour=int(time[:2])
    time_min=int(time[3:5])
    time_second=int(time[6:8])
    
    sum_hour=time_hour*3600
    sum_min=time_min*60
    sum_second=time_second
    
    sum=sum_hour+sum_min+sum_second
    
    print(time,'hour =',sum,'second')
       
elif (hour_or_second=='2' or hour_or_second=='second'):
  
   time=int(input('enter the second : '))  
       
   time_hour=time//3600
   time_min=(time-(time_hour*3600))//60
   time_second=(time-((time_hour*3600)+time_min*60)) 
   
   if time_hour<10:
       time_hour='0'+str(time_hour)
   if time_min<10:
       time_min='0'+str(time_min)   
   if time_second<10:
       time_second='0'+str(time_second)
         
   print(time_hour,':',time_min,':',time_second,sep='')
   
       
