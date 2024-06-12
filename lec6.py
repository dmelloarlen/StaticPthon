# try:
#     print(y)
# except Exception as e:
#     print(e)

#    a= input("enter:")
#    c = a+9
# except Exception as e:
#    print(e)
# finally:
#   print("y")

# try:
#     i=int('string')
# except IOError as e:
#     print(f"hello {e}")
# except ValueError as e:
#     print(f"hello2 {e}")

# try:
#     r=10/0
# except ZeroDivisionError as e:
#     print("Divide error")

# try:
#     r='2'+2
# except TypeError as e:
#     print(f"Error!!!!!!!!! {e}")

# try:
#     Logging.log(round(24.60/3.5,4))
# except FloatingPointError as e:
#     print(f"Error {e}")


# bulid in libraries
# import math
# import random
# import hashlib
# import pathlib
# import os

#calling functions from different file syntax and example
# from filename import function name

# from lec5 import sum
# print(sum(2,3))

# from package import mod1
# print(mod1.sum(2,3))

# from package.pack1 import mod2
# print(mod2.Mul(2,3))

try:
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
            print(n1+n2)
        elif ch==2:
            print(n1-n2)
            continue 
        elif ch==3:
            print(n1*n2)
            continue 
        elif ch==4:
            print(n1/n2)
            continue 
        elif ch==5:
            break
        else:
            print("entr a valed ")
            
except ZeroDivisionError:
    print("Exception:Cannot divide by zero")













