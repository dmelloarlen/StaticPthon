#Initialization
list=[]
name=[]
rating=[]
comment=[]
#Defining functions
def get_ratings(f):

    for line in f:
        list.append(line.strip())

def read_feedback():
    try:
        #Opening files
        f1=open("feedback1.txt",'r') 
        f2=open("feedback2.txt",'r') 
        f3=open("feedback3.txt",'r') 

        #Functions call
        get_ratings(f1)
        get_ratings(f2)
        get_ratings(f3)

        #Logic
        for i in range(len(list)):
            name.append(list[i].split()[0].split(":")[0])
            rating.append(list[i].split()[1])
            comment.append(list[i].split("-")[1])

        sum=0
        for i in rating:
            sum+=int(i)
        sum=sum/len(name)

        #Closing files
        f1.close()
        f2.close()
        f3.close()
        return sum

    except(FileNotFoundError):
        print("File not found",FileNotFoundError)

def create_feedback():
    try:
        open("feedback_summary.txt",'x')
    except(Exception):
        print("File already exists",Exception)

def write_feedback(avg):
    create_feedback()
    try:
        fs=open("feedback_summary.txt",'w')
        fs.writelines(f"Total Feedback Entries:{len(list)}\n")
        fs.writelines(f"Average Rating: {round(avg,2)}\n")

        fs.writelines("\nFeedbacks:\n")
        for feedbacks in list:
            fs.writelines(f"{feedbacks}\n")

    except(Exception):
        print("error",Exception)

#Functions call
avg=read_feedback()
write_feedback(avg)