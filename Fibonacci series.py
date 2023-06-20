a=0
b=1
#n is for the number upto which you wanna print the series till
n=int(input("Enter the number upto which you wanna print the fibonacci seires:"))
print(a)
for i in range(n+1):
    print(b)
    sum1=a+b
    a=b
    b=sum1
