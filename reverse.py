n=int(input("enter the number to be reversed"))
rev=0
while(n!=0):    
    s=n%10
    rev=rev*10+s
    n=int(n/10)
print(rev)    
