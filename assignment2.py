s=set()
def add_book(title,author,genre):
    tuple=title,author,genre
    return tuple

def add_to_library(list,tuple):
    if tuple not in list:
        list.append(tuple)
        print("sucessfull!!!")
    else:
        s.add(tuple)
        print("already exists!!!!!")

def remove_from_library(list,title):
    x=True
    for i in range(len(list)):
        if list[i][0] == title:
            print("removed",list[i])
            list.remove(list[i])
            x=False
    if x:
        print("No match found")

def list_books(list):
    if len(list)==0:
        print("No books yet")
    else:
        for i in range(len(list)):
                print(list[i])

def search_books(list,search):
    x=True
    for i in range(len(list)):
        if list[i][0] == search or list[i][1]==search:
            print(list[i])
            x=False
    if x:
        print("No match found")
        
def categorize_books(list):
    dict={}
    if not list:
        print("No books in the library to categorize.")
        return
    dict.clear()
    for i in list:
        genre = i[2]
        if genre not in dict:
            dict[genre] = []
        dict[genre].append(i)

    for genre,books in dict.items():
        print(f"Genre: {genre}")
        for book in books:
            print("  Title:", book[0])
            print("  Author:", book[1])
            print("_______________")

def list_duplicates():
    if not s:
        print("No duplicates in the library.")
        return

    print("Duplicate books (entries that were attempted to be added again):")
    for book in s:
        print("Title:", book[0])
        print("Author:", book[1])
        print("Genre:", book[2])

list=[]
while True:
    print("1.Add a book\n2.Remove a book\n3.Search a book\n4.List all books\n5.Catogrized\n6.Dublicate books\n7.Exit")
    ch=int(input("Enter your choice:"))
    print("----------------------------------------------------------------------------")

    if ch==1:
        title=input("Enter title:")
        author=input("Enter author:")
        genre=input("Enter genre:")
        add_to_library(list,add_book(title,author,genre))
    elif ch==2:
        title=input("Enter title:")        
        remove_from_library(list,title)
    elif ch==3:
        search=input("Enter title or author:")
        search_books(list,search)
    elif ch==4:
        list_books(list)
    elif ch==5:
        categorize_books(list)
    elif ch==6:
        list_duplicates()
    elif ch==7:
        print("Exiting......")
        break
    else:
        print("Invalid choice")
    print("----------------------------------------------------------------------------\n")



