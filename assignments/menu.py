class MenuItems:
    name=[]
    price=[]
    quantity=[]
    menu=[]

    def add_item(obj,name,price,quantity):
        obj.menu.append([name,price,quantity])
        print("Product Added sucessfully!!")

    def update_item(obj,n1,name,price,quantity):
        x=True
        for i in obj.menu:
            if i[0]==n1:
                i[0]=name
                i[1]=price
                i[2]=quantity
                print("Update sucessfull!!")
                x=False
        if x:
            print("Items not found!!") 
    
    def delete_item(obj,name):
        x=True
        for i in obj.menu:
            if i[0]==name:
                obj.menu.remove(i)
                print("Item removed sucessfully!!",obj.menu)
                x=False
        if x:
            print("Item not found!!")
    
    def display_menu(obj):
        for i in obj.menu:
            print(f"{i[0]} {i[1]} {i[2]}")
            print()
    
    def read_menu_from_file(obj):
        try:
            file=open("menu.txt","r")
            if file!='':               
                for lines in file:
                    obj.menu.append([lines.split(' ')[0],lines.split(' ')[1],lines.split(' ')[2]])
        except( FileNotFoundError):
            print("File not found!!")
    
    def write_menu_to_file(obj):
        try:
            file=open("menu.txt","w+")
            for i in obj.menu:
                file.write(f"{i[0]} {i[1]} {i[2]} \n")
            print("Saved sucessfully!!")
        except( FileNotFoundError):
            print("File not found!!")