import os
print (

'''
╔═══╗      ╔╗            ╔╗       ╔╗
║╔═╗║      ║║            ║║      ╔╝╚╗
║║ ╚╝ ╔══╗ ║║  ╔══╗ ╔╗╔╗ ║║  ╔══╗╚╗╔╝ ╔══╗ ╔═╗
║║ ╔╗ ║╔╗║ ║║  ║╔═╝ ║║║║ ║║  ║╔╗║ ║║  ║╔╗║ ║╔╝
║╚═╝║ ║╔╗║ ║╚╗ ║╚═╗ ║╚╝║ ║╚╗ ║╔╗║ ║╚╗ ║╚╝║ ║║
╚═══╝ ╚╝╚╝ ╚═╝ ╚══╝ ╚══╝ ╚═╝ ╚╝╚╝ ╚═╝ ╚══╝ ╚╝
''') 

#first read this------------\
#                           |
#                           |
#                           /          
#                          √
 
print(
   
'''

Your Calculation
for addition : type 'add'
for multiplication:'multiply'
for division : 'divide'
forb subtration : 'subtract'
for square root: 'root'
for cancle processing:'exit'
''')
while True:
   user_input = input()
   
   if user_input == "exit":
     os.system('clear')
     break 
    
   elif user_input== 'add':
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter b number: "))
    result= (num1 +num2)
    print(result)
      
   elif user_input=='multiply':
     num1 =float(input("Enter a number: "))
     num2 =float(input("Enter b number: "))
     result=(num1*num2)
     print(result)
   elif user_input=='divide':
     num1 =float(input(""))
     num2 =float(input(""))
     result =(num1 //num2)
     print(result)

   elif user_input=='subtract':
     num1 =float(input(""))
     num2 =float(input(""))
     result =(num1 - num2)
     print(result)


   elif user_input=='root':
     num1 =float(input(""))
     num2 =float(input(""))
     result1 = (num1**1/2) 
     result2=  (num2**1/2) 
     print(result1)
     print(result2 )
