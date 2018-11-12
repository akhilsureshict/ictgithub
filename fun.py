def add(x,y):
    z=x+y
    print("sum is" ,z)
def sub(x,y):
    z=x-y
    print("difference is ",z)
def multiply(x,y):
    z=x*y
    print("product is",z) 
def division(x,y):
    z=x/y
    return z       
a=int(input("enter a"))
b=int(input("enter b"))
add(a,b)    
sub(a,b)
multiply(a,b)
q=division(a,b)
print(q)