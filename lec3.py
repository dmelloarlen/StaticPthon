#Dicnary compreantion
# cub={x:x**3 for x in range(1,11)}
# print(cub)

#list conpreantion
# y=4
# list=[x*y for x in range(101,121)]
# print(list)

# y=4
# list=[x for x in range(1,29) if x%2==0]
# print(list)

# list=[]
# n=int(input("Enter the size:"))
# for i in range(n):
#     val=int(input(f"Enter value {i+1}:"))
#     list.append(val)
# print(list)

#Function decleration
# def sum():
#     sum=0 byh,
#     for i in range(1,6):
#         sum+=int(input(f"Enter value {i}:"))
#     return sum

# print(sum())
# list=[]
# def age():
#     n=int(input("enter no of students"))
#     for i in range(n):
#        val=int(input(f"Enter age {i}:")) 
#        list.append(val) 
#     print(sum(list))
# age()

#Inline function
# add=lambda x,y: x+y
# sub=lambda x,y: x-y
# mul=lambda x,y: x*y
# div=lambda x,y: x/y
# sqrt=lambda x: x**2

# print(add(2,3))
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))
# print(sqrt(2))

#Arbitrary arguments (*args)
# def sum(*num):
#     return num[0]+num[1]

# print(sum(2,3))