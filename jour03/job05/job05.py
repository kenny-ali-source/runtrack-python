def calcule(num1, operator, num2):
    result=0
    if operator == "+":
        result = num1 +  num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '/':
        result = num1 / num2
    else :
        print("error")

    return result
print(calcule(2, '+' ,5))
    
    

