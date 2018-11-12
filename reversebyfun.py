def reverse(n):
    rev=0
    while(n!=0):    
        s=n%10
        rev=rev*10+s
        n=n//10
    return rev    

num=int(input("enter the number to be reversed"))
r=reverse(num)
print("the reverse form is",r)

    
