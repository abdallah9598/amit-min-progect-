

for i in range(1,10000):
  try: 
     num1 = float(input('please inter num 1 :'))
     operator = input('plese inter operators :')
     num2 = float(input('please inter num 2 :'))
  
       
     def sum1(x):
           if operator == '+':
             return num1 + num2
     if operator == '+': 
         print(sum1(4))
           

     def mun1(x):
           if operator == '-':
             return num1 - num2
     if operator == '-': 
             print(mun1(4))
     

     def dot(x):
           if operator == '*':
             return num1 * num2
     if operator == '*': 
             print(dot(4))    
     

     def mm(x):
           if operator == '/':
             return num1 / num2
     if operator == '/': 
             print(mm(4))    
     
     def mud(x):
           if operator == '%':
              return num1 % num2
     if operator == '%': 
             print(mud(4))    
               
     finsh = (input('if you need another operators')) 

     if finsh == 'yes':
         print(i) 
     else:
         print('thank for you')
         break
  except:
       print('your input is wrong please try again')