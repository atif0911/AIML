#if-else
isMale=True
if isMale: #if ismale is true 
    print("U r a male")
else: #if ismale is not true
    print("U r a female")

#we can use 'and' 'or' 'not(isMale)' with conditions  
isTall=True
if isMale and isTall:
    print("Great")
elif not(isMale) and isTall:
    print("Okay")
else:
    print("haha")

#using comparisons now
def max(num1,num2,num3):
    if num1>=num2 and num1>=num3: #>= <= > < !=
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
    
print(max(8,1,5))