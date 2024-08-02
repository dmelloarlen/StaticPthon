def celToFer(n1):
    return ((9/5)*n1 + 32)

def ferToCel(n1):
    return ((n1-32) * 5/9)

l=1
while l==1:
    n1=int(input("Enter the temperature:"))
    print("******************************************")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.exit")
    ch=int(input("Enter your choice for conversion:"))
    if ch==1:
        print(celToFer(n1))
        continue
    elif ch==2:
        print(ferToCel(n1))
        continue 
    elif ch==3:
        l=0
        continue 
    else:
        print("wrong choice")
        continue
