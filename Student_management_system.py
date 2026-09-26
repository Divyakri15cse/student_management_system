#CRUD operation of Student Data using File Handling
import os
choice='y'
while choice=='y' or choice=='Y':
    print("\n------Menu------")
    print("1.Add Record")
    print("2.Show All Records")
    print("3.Search Record")
    print("4.Delete Record")
    print("5.Update Record")
    ch=int(input("Enter Your Choice(1,2,3,4 or 5):"))
    if ch==1:
        roll=input("Enter Roll:")
        name=input("Enter Name:")
        course=input("Enter Course:")
        fee=input("Enter Fee:")
        record=roll+" "+name+" "+course+" "+fee+"\n"
        file=open("StudentData.txt","a")
        file.write(record)
        file.close()
        print("Record Sucessfully Added To File...")
    elif ch==2:
        print("-----------------------------------------------------------------")
        print("Roll"+"\t"+"Name"+"\t"+"Course"+"\t"+"Fee")
        print("-----------------------------------------------------------------")
        file=open("StudentData.txt","r")
        lst=file.readlines()
       
        for x in lst:
            record=x.split(" ")
            print(record[0]+"\t"+record[1]+"\t"+record[2]+"\t"+record[3],end="")
        file.close()
        print("-----------------------------------------------------------------")
    elif ch==3:
        flag=False
        r=input("Enter roll to search:")
        file=open("StudentData.txt","r")
        txt=file.readline()
        print("-----------------------------------------------------------------")
        print("Roll"+"\t"+"Name"+"\t"+"Course"+"\t"+"Fee")
        print("-----------------------------------------------------------------")
        while txt!="":
            record=txt.split(" ")
            if record[0]==r:
               print(record[0]+"\t"+record[1]+"\t"+record[2]+"\t"+record[3],end="")
               flag=True
               break
            txt=file.readline()
        if flag==False:
            print("Record not found for roll:",r)
        print("-----------------------------------------------------------------")
        file.close()
    elif ch==4:
        flag=False
        r=input("Enter roll to delete:")
        ofile=open("StudentData.txt","r")
        tfile=open("Temp.txt","w")
        txt=ofile.readline()
        while txt!="":
             record=txt.split(" ")
             if record[0]!=r:
                tfile.write(txt)
             else:
                flag=True
             txt=ofile.readline()
        ofile.close()
        tfile.close()
        os.remove("StudentData.txt")
        os.rename("Temp.txt","StudentData.txt")
        if flag==False:
            print("Record not found to delete for roll:",r)
        else:
            print("Record deleted successfully")
    elif ch==5:
        flag=False
        r=input("Enter roll to update:")
        ofile=open("StudentData.txt","r")
        tfile=open("Temp.txt","w")
        txt=ofile.readline()
        while txt!="":
             record=txt.split(" ")
             if record[0]!=r:
                tfile.write(txt)
             else:
                 name=input("Enter Name:")
                 course=input("Enter Course:")
                 fee=input("Enter Fee:")
                 nrecord=r+" "+name+" "+course+" "+fee+"\n"
                 tfile.write(nrecord)
                 flag=True
             txt=ofile.readline()
        ofile.close()
        tfile.close()
        os.remove("StudentData.txt")
        os.rename("Temp.txt","StudentData.txt")
        if flag==False:
            print("Record not found to update for roll:",r)
        else:
            print("Record updated successfully")  
    else:
        print("Invalid Choice...")
    choice=input("Do you want to continue(y/n):")
