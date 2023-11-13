x=int(input("value of x"))
y=int(input("value of y"))
n=int(input("no to be divisible by"))
i=x+1
while(i>x and i<=y):
    i=i+1
    if i%n==0:
        print(i)