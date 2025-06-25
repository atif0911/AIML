#version 1
# #very basic calculator lol
# num1=input("Enter a number : ")
# num2=input("Enter another number : ")
# result=num1+num2 #string 
# print(result)
# result=float(num1)+float(num2) #convert to int/float
# print(result)

#version 2
num1=float(input("Enter a number"))
op=input("Enter operator:")
num2=float(input("Enter a number"))
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='/' and num2!=0:
    print(num1/num2)
elif op=='*':
    print(num1*num2)
elif op=='%':
    print(num1%num2)
else:
    print("invalid choice")