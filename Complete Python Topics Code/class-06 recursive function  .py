# Recursive function
# to compute the factorial of non - negative Number
# 5! = 1x2x3x4x5

n = int(input("Enter a value to get factorail: "))

def fac(n):
    if n > 0 :
        result = n * fac(n-1)
        print(result)
    else:
        result=1
        
    return result

factorial = fac(n)

print(f"Factorial of {n} = {factorial}")
