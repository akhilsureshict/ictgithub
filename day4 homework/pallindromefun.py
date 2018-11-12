def pallindrome(x):
    g=x
    rev=0
    while(x!=0):
        s=x%10
        rev=rev*10+s
        x=x//10
    if (g==rev):    
        return"pallindrome number"
    else:
        return"not a pallindrome nujmber"
n=int(input("enter the number")) 
result=pallindrome(n)           
print(result)
