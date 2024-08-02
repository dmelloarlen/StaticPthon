import subprocess
import data_cleaning2 as dc


while True:
    print("----------------------------------------------------------------------------")
    print("1.Find null values\n2.Find duplicate values\n3.Start streamlit dashboard\n4.Exit\n")
    ch=int(input("Enter your choice:"))
    print("----------------------------------------------------------------------------")
    if ch==3:
        subprocess.run('streamlit run dashboard.py', shell=True)
    elif ch==4:
        break
    else:
        dc.cleaning(ch)


