# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:34:03 2023

@author: Dell
"""
from min import * 

for i in range(1,11):
   
     num1 = float(input('please inter num 1 :'))
     operator = input('plese inter operators :')
     num2 = float(input('please inter num 2 :'))

     if operator == '+':
        sum1(num1,num2)
     if operator == '-':
         subtract(num1,num2)
     if operator == '*':
         dot(num1,num2)
     if operator == '/':
         division(num1,num2)

     if operator == '%':
         mud(num1,num2)
         
     ch = input('do another? y/n : ')
     if ch == 'y':
        continue
     else:
        break