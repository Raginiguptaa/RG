def add(a,b):
    return a+b

def sub(a,b):
    return a-b if a>b else b-a

    
def division(a,b):
    return a/b 

def multiply(a,b):
    return a*b 

# def add(a,b):
#     return a+b      


# def main():
while True:
    a=int(input("enter your first number\n"))
    b=int(input("enter your second number\n"))
    ans=0
    c=input("What operation you want to perform??\n")
    if c=="+":
        ans= add(a,b)
    elif c=="-":
        ans= sub(a,b)
    elif c=="*":
        ans= multiply(a,b)    
    else:
        ans= division(a,b)    



    print(ans)
    print("________________________NEW CALCULATIONS__________________________")