print(2**3) #exponent '**' like '^'

def exp(num,pow):
    result=1
    for i in range(pow):
        result*=num
    return result

num=float(input("Enter Num "))
pow=int(input("enter power "))
print(exp(num,pow))