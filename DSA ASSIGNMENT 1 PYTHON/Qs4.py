#   Consider the given series and calculate the summation up-to ‘N’ number. 1+1+4+9+25+64+ .......... +N    



def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    


sum=0
fibsq=0
n=int(input("Enter no. of numbers:"))
for i in range(1,n+1):
    fibsq=fibonacci(i)**2
    sum+=fibsq
print("Sum of the series is ",sum)