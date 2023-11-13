n=int(input("enter any number n "))
f=1
i=1
count=0
while count<n:
    f=f*i
    i=i+1
    count=count+1
print("the factorial of ",n," is ",f)