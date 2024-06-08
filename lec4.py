#Slicing
# tuple=(1,2,3,4,5,6,7)
# print(tuple[1:3])

#continue,break,pass
# for i in range(1,11):
#     if i!=7:
#         print(i)
#         continue
#     else:
#         break

# for i in range(1,11):
#     pass


# list=["Arlen","Aarya","Maadhav"]
# def find():
#     name=input("Enter name of student:")
#     if name=="Arlen":
#         print("found")
#     else:
#         find()

# find()



# list=["Arlen","Aarya","Maadhav"]
# ln=len(list)
# def find(name,list,ln,i=0):
#     i1=i
#     x=0
#     if ln!=0:
#         if list[i1]==name:
#             x=1
#         else:
#             i1=i1+1
#             # find(name,list,(ln-1),i1)

#         ln-=1
#     return x

# x1=find("Maadav",list,ln,0)

# if x1!=1  :
#         print("not found")
# if x1==1:
#      print("found")

#class creation
# class Class1:
#     name="Arlen"
#     roll=4
#     def show(self):
#         print(f"{self.name} and {self.roll}")

# obj=Class1()
# obj.name="Aarya"
# obj.roll=11
# obj.show()


# class Bird:
#     def __init__(self):
#         print("Bird")
# class Peguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print("peguin")

# obj1=Peguin()

list=[3,2,2,3]
val=3

list2=[list[i] for i in range(0,len(list)) if list[i]!=val]
print(list2)

                


