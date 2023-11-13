n=int(input("enter any no "))
count=2
while count<n:
    p=n%count
    if p!=0:
        count=count+1
        print("n is a prime no.")
        break
    else:
        print("n is composite no.")
        break