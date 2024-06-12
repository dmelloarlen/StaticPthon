# class C1:
#     def __init__(self,n,r):
#         print("p constructor")
#         self.name=n
#         self.r_no=r
#     def call(self):
#         print(f"name={self.name} roll={self.r_no}")

# object=C1("Arle",4)


# class Base:
#     def __init__(self):
#         self.__a=4

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("protected of base",self.__a) 

#         self.__a=3
#         print("protected of base",self.__a)

# obj=Derived()


# class vehical:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year

# class Car(vehical):
#     def move(self):
#         print("water")
# class Boat(vehical):
#     def move(self):
#         print("water")
# class Plane(vehical):
#     def move(self):
#         print("air")

# car=Car("fortuner",2024)
# boat=Boat("boat1",2024)
# plane=Plane("beoing777",2024)4

# for  i in (car,boat,plane):
#     print(i.brand)
#     print(i.year)

# class student:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

# class branch(student):
#     def __init__(self,name,id,b):
#         super().__init__(name,id)
#         self.b = b

# i = branch('Arlen', '898','cse')
# print(i.name)
# print(i.id)
# print(i.b)

# class Mother:
#     def __init__(self,mname) -> None:
#         self.name=mname
# class Father:
#     def __init__(self,fname) -> None:
#         self.name=fname
# class Surname:
#     def __init__(self,sname) -> None:
#         self.name=sname
# class Child(Mother,Father,Surname):
#     def __init__(self,name,mname,fname,sname) -> None:
#         self.name=name
#         Father.__init__(self,fname)
#         Mother.__init__(self,mname)
#         Surname.__init__(self,sname)
#         print(name,fname,sname,mname)

# obj=Child("yug","Aarya","Maadhav","paj")


# def dec(func):
#     def process():
#         print("welcome")
#         func()
#         print("goodbye")
#     return process

# @dec 
# def yes():
#   print("Arlen")

# yes()

#file handling

# file=open("file.txt","w")
# file.write("Hello")
# file.close()

# with open("file.txt","r") as file:
#     content=file.read()
#     print(content)

# with open("file.txt","r") as file:
#     for line in file:
#         print(line.strip())

# with open("file.txt","a") as file:
#     file.write(" world")

# with open("file.txt","r") as file:
#     file.seek(2)
#     content=file.read()
#     print(content)

def sum(x,y):
    return x+y







        

    
    