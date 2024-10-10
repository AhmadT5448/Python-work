def infocoll():
    global x
    global y
    x=int(input("please enter the number to perform calculation"))
    y=int(input("please enter another number to perform calculation"))
    
def add():
    print(x+y)
    
def subtract():
    print(x-y)
    
def multiply():
    print(x*y)
    
def divide():
    print(x/y)
    
def expo():
    x=int(input("please enter the number to perform calculation\n"))
    y=int(input("please enter the power you want to take\n"))
    print(x**y)
    
def squreroot():
    x=float(input("please enter the number to perform calculation\n"))
    print(x**0.5)

def thirdroot():
    x=float(input("please enter the number to perform calculation\n"))
    print(x**0.33333)
def factorial():
    factorial=1
    x=int(input("please enter the number to perform calculation\n"))
    if x < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,x + 1):
            factorial = factorial*i
        print("The factorial of",x,"is",factorial)
    
    
    
    
    
def main():
    
    print("\t\t\tHello welcome to the calcultor\n")
    a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
    
    while a!=0:
        if a==1:
            infocoll()
            add()
            a=int(input("press 0 if you want to  exit\n press 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        
        if a==2:
            infocoll()
            subtract()
            a=int(input("press 0 if you want to  exit\n press 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        
        if a==3:
            infocoll()
            multiply()
            a=int(input("press 0 if you want to  exit\n press 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        
        if a==4:
            infocoll()
            divide()
            a=int(input("press 0 if you want to  exit\npress 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        
        if a==5:
            expo()
            a=int(input("press 0 if you want to  exit\npress 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        
        if a==6:
            squreroot()
            a=int(input("press 0 if you want to  exit\npress 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
           
        if a==7:
            thirdroot()
            a=int(input("press 0 if you want to  exit\npress 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
        if a==8:
            factorial()
            a=int(input("press 0 if you want to  exit\npress 9 if you want to go back to menu"))
            if a==0:
                print("\t\t\t\thave a good day")
                exit
            if a==9:
                a=int(input("please select from below what function you want to perform\n\n select 1 if you want to perform additon\n select 2 if you want to perform subtraction\n select 3 if you want to perform multiplication\n select 4 if you want to perform Division\n select 5 if you want to perform exponantial\n select 6 if you want to perform square root\n select 7 if you want to perform third root\n select 8 if you want to perform factorial\n"))
           
    
    
main()
    