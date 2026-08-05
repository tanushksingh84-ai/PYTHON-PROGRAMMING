"""
for i in range(1,101):
    if i//3==0:
        print("Fizz")
    elif i//5==0:
        print("Buzz")
    elif i//3==0 and i//5==0:
        print("fizz & buzz")
    else:
        print("no numbers is divisible by 5 and 3")
        """

def countdigits(num):
    a=0
    while num>0:
        n=n//10
        a+=1
        print(a)

def rev(n):
    a=0
    temp=n
    while n>0:
        b=n//10
        a=a*10+(n-b*10)
        n=n//10
    if n==temp:
        print("Reversed")
    else:
        print("Not Reversed","/n",a)

def largest(n):
    a=0
    n=list(str(n))
    print(int(max(n)))

def smallest(n):
    a=0
    n=list(str(n))
    print(int(min(n)))

def sumandpro(n):
    n=list(str(n))
    a,b=0,1
    for i in n:
        a+=int(i)
        b*=int(i)
    print("sum is=","/n",a)
    print("Product is =","/n",b)



