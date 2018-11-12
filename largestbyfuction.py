def largest(a,b,c):
   if(a>b):
       if(a>c):
           return a
       else:
           return c
   else:
        if(b>c):
            return b
        else:
            return c               
    
x=int(input("enter first number")) 
y=int(input("enter second numbers"))
z=int(input("enter third number"))
l=largest(x,y,z)
print(l) 

