import exception2 as e
class Order:
    list=[]
    price=[]
    q=1
    def calculate_total(obj):
        sum=0
        gst=40
        discount=30
        print("******************Recipt************************")
        for i in obj.list:
            print(f"|{i[0]} {i[1]} {i[2]}|")
            print()
            sum+=(int(i[1])*int(i[2]))
        print("______________________________")
        print(f"Total:{sum}")
        print(f"GST:{gst}")
        print(f"Discount:{discount}")
        print("_______________________")
        print(f"Grand total:{(sum)+gst-discount}")

    def take_order(obj,menu):
        while True:
            n=input("Enter the name of item you want to order else press 'Enter':")
            if n=='':
                obj.write_order_to_file(obj)
                break
            else:
                obj.q=input("Enter the quantity of item you want to order:")
                x=True
                try:
                    for i in menu:
                        if i[0]==n:
                            if int(i[2])<int(obj.q):
                                raise(e.InsufficientQuantityError("Quantity is not available!!"))
                            else:
                                obj.list.append([i[0],i[1],obj.q])
                                obj.price.append(i[1])
                            x=False
                    if x:
                        raise(e.InvalidMenuItemError("Items not found!!"))
                    continue
                except e.InsufficientQuantityError as err:
                    print(err.err)
                    continue
                except e.InvalidMenuItemError as err:
                    print(err.err)

        print("________________________________")
        obj.calculate_total(obj)
    
    def read_order_from_file(obj):
        try:
            file=open("order.txt","r")
            if file!='\n':               
                for lines in file:
                    obj.list.append([lines.split(' ')[0],lines.split(' ')[1],lines.split(' ')[2]])
        except( FileNotFoundError):
            print("")
    
    def write_order_to_file(obj):
        try:
            file=open("order.txt","w+")
            for i in obj.list:
                file.write(f"{i[0]} {i[1]} {i[2]} \n")
                # file.write()
            print("Saved sucessfully!!")
        except( FileNotFoundError):
            print("")
