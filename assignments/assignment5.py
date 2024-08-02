import datetime as dt
list=[]
dict={}
name=[]
category=[]
price=[]
quantity=[]
expiration=[]

class product:
    def add_product_to_inventory():
        n=input("Enter name of product:")
        c=input("Enter category of product:")
        p=int(input("Enter price of product:"))
        q=int(input("Enter quantity of product:"))
        e=input("Enter expiration date of product:")
        list.append([n,c,p,q,e])
        print("Product Added sucessfully!!")
    
    def remove_product_from_inventory():
        n=input("Enter the name of product to be removed:")
        x=True
        for i in list:
            if i[0]==n:
                list.remove(i)
                print("Product removed sucessfully!!")
                x=False
        if x:
            print("Product not found!!")
    
    def search_products():
        n=input("Enter the name of product to be searched:")
        x=True
        for i in list:
            if i[0]==n:
                print(i)
                print("Product found!!")
                x=False
        if x:
            print("Product not found!!")

    def list_all_products():
        for i in list:
            print(i)
            print()
        
    def expiration_date():
        currentDate=dt.date.today().strftime("%d-%m-%Y")
        x=True
        for i in list:
            if int(i[4].split('-')[0])<=int(currentDate.split("-")[0]) and int(i[4].split('-')[1])<=int(currentDate.split("-")[1]) and int(i[4].split('-')[2])<=int(currentDate.split("-")[2]):
                print(i)
                list.remove(i)
                print("Expired Products removed sucessfully!!")
                x=False
        if x:
            print("Expired Product not found!!")
    
    def cetegorize_products():
        if not list:
            print("No products t.")
            return
        dict.clear()
        for i in list:
            cat = i[1]
            if cat not in dict:
                dict[cat] = []
            dict[cat].append(i)

        for key,val in dict.items():
            print(f"cat: {key}")
            print("____________________")
            for val in val:
                print("|  Name:", val[0])
                print("|  price:", val[2])
                print("|  Quantity:", val[4])
                print("|  Date:", val[3])
                print("____________________")
            print("__________________________________________________")

    def load_from_inventory():
        try:
            file=open("inventory.txt","r")
            if file!='\n':               
                for lines in file:
                    list.append([lines.split(' ')[0],lines.split(' ')[1],lines.split(' ')[2],lines.split(' ')[3],lines.split(' ')[4]])
                    # lines.strip("\n")
        except( FileNotFoundError):
            print("File not found!!")
            
    def save_to_inventory():
        try:
            file=open("inventory.txt","w+")
            for i in list:
                file.write(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} \n")
                # file.write("\n")
            print("Saved sucessfully!!")
        except( FileNotFoundError):
            print("File not found!!")

obj=product
obj.load_from_inventory()
while True:
    # list.clear()
    print("1.Add a product\n2.Remove a product\n3.Search a product\n4.List all products\n5.Catogrize products\n6.Remove expired products\n7.Save changes\n8.Exit\n")
    ch=int(input("Enter your choice:"))
    print("----------------------------------------------------------------------------")

    if ch==1:
        obj.add_product_to_inventory()
    elif ch==2:
        obj.remove_product_from_inventory()
    elif ch==3:
        obj.search_products()      
    elif ch==4:
        obj.list_all_products()
    elif ch==5:
        obj.cetegorize_products()
    elif ch==6:
        obj.expiration_date()
    elif ch==7:
        obj.save_to_inventory()
    elif ch==8:
        print("Exiting......")
        break
    else:
        print("Invalid choice")
    print("----------------------------------------------------------------------------\n")


        






    

