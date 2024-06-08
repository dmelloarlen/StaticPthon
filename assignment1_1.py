def add(n1,n2):
    return (n1+n2)
def sub(n1,n2):
    return (n1-n2)
def mul(n1,n2):
    return (n1*n2)
def div(n1,n2):
    return (n1/n2)
    
def calculator():
    while True:
        n1=int(input("Enter num 1:"))
        n2=int(input("Enter num 2:"))
        print("******************************************")
        print("1.Add")
        print("2.Sub")
        print("3.mul")
        print("4.div")
        print("5.exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print(add(n1,n2))
        elif ch==2:
            print(sub(n1,n2))
            continue 
        elif ch==3:
            print(mul(n1,n2))
            continue 
        elif ch==4:
            print(div(n1,n2))
            continue 
        elif ch==5:
            break
        else:
            print("wrong choice")
            continue

calculator()