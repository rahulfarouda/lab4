n=int(input("input the no."))
a=1
b=2
count=0
if n<0:
    print("invalid input")
elif n==0:
    print("1")
elif n>0:
    while count<n:
        s=a+b
        print(s)
        a=b
        b=s
        count=count+1