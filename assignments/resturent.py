import menu as m
import order as o

objm=m.MenuItems
objo=o.Order
objm.read_menu_from_file(objm)
objo.read_order_from_file(objo)

while True:
    # list.clear()
    print("1.Add a item\n2.Delete a item\n3.Update a product\n4.Display menu\n5.Place order\n6.Print recipt\n7.Save changes\n8.Exit\n")
    ch=int(input("Enter your choice:"))
    print("----------------------------------------------------------------------------")
    

    if ch==1:
        n=input("Enter name of item:")
        p=int(input("Enter price of item:"))
        q=int(input("Enter quantity of item:"))
        objm.add_item(objm,n,p,q)
    elif ch==2:
        n=input("Enter the name of item to be removed:")
        objm.delete_item(objm,n)      
    elif ch==3:
        n1=input("Enter the name of item to be updated:")
        n=input("Enter name of item:")
        p=int(input("Enter price of item:"))
        q=int(input("Enter quantity of item:"))
        objm.update_item(objm,n1,n,p,q)
    elif ch==4:
        objm.display_menu(objm)
    elif ch==5:
        objo.take_order(objo,objm.menu)     
    elif ch==6:
        objo.calculate_total(objo)
    elif ch==7:
        objm.write_menu_to_file(objm)
    elif ch==8:
        print("Exiting......")
        break
    else:
        print("Invalid choice")
    print("----------------------------------------------------------------------------\n")

