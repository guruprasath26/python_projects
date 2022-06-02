from tkinter import *
import tkinter.messagebox as messageBox
import mysql.connector as mysql


root =Tk()
root.geometry("600x300")
root.title("python+Tkinter+mysql")


def insert():
    employeeid=e_employeeid.get()
    employeename=e_employeename.get()
    salary=e_salary.get()
    city=e_city.get()


    if(employeeid==""or employeename=="" or salary=="" or city==""):
        massageBox.showinfo("insert status","All Fields are requried")
    else:
        con =mysql.connect(host="localhost",user="root",password="",database="employeeinfo")
        cursor=con.cursor()
        cursor.execute("insert into  employeedetails  values ('" + employeeid +"','"+employeename +"','" + salary + "', '" +city +"')")
        cursor.execute ("commit");

        e_employeeid.delete(0,'end')
        e_employeename.delete(0,'end')
        e_salary.delete(0,'end')
        e_city.delete(0,'end')
        show()
        messageBox.showinfo("insert status","inserted successfully");
        con.close();
    

def delete():
    if (e_employeeid.get()==""):
        messageBox.showinfo("Delete status", "employeeid is complosury for delete")
    else:
        con =mysql.connect(host="localhost",user="root",password="",database="employeeinfo")
        cursor=con.cursor()
        cursor.execute("delete from employeedetails where employeeid='"+e_employeeid.get() +"'")
        cursor.execute ("commit");

        e_employeeid.delete(0,'end')
        e_employeename.delete(0,'end')
        e_salary.delete(0,'end')
        e_city.delete(0,'end')
        show()
        messageBox.showinfo("Delete status","Deleted successfully");
        con.close();



def update():
    employeeid=e_employeeid.get()
    employeename=e_employeename.get()
    salary=e_salary.get()
    city=e_city.get()


    if(employeeid==""or employeename=="" or salary=="" or city==""):
        massageBox.showinfo("Update status","All Fields are requried")
    else:
        con =mysql.connect(host="localhost",user="root",password="",database="employeeinfo")
        cursor=con.cursor()
        cursor.execute("update  employeedetails  set employeename='"+ employeename +"',salary='"+salary+"',city='"+city+"' where employeeid='"+employeeid+"'")
        cursor.execute ("commit");

        e_employeeid.delete(0,'end')
        e_employeename.delete(0,'end')
        e_salary.delete(0,'end')
        e_city.delete(0,'end')
        show()
        messageBox.showinfo("Update status","Updated successfully");
        con.close();
    
def get():
     if (e_employeeid.get()==""):
        messageBox.showinfo("Fetch status", "employeeid is complosury for delete")
     else:
        con =mysql.connect(host="localhost",user="root",password="",database="employeeinfo")
        cursor=con.cursor()
        cursor.execute("select * from employeedetails where employeeid='"+e_employeeid.get() +"'")
        rows=cursor.fetchall()

        for roe in rows:
            e_employeename.insert(0,row[1])
            e_salary.insert(0,row[2])
            e_city.insert(0,row[3])
      
        con.close();


def show():
    con =mysql.connect(host="localhost",user="root",password="",database="employeeinfo")
    cursor=con.cursor()
    cursor.execute("select * from employeedetails")
    rows=cursor.fetchall()
    list.delete(0, list.size())


    for row in rows:
            insertData=str(row[0])+'               '+row[1]
            list.insert(list.size()+1, insertData)
    con.close()    
    
    







    
employeeid=Label(root,text='employee id',font=('bold',10))
employeeid.place(x=20,y=30)

employeename=Label(root,text='employee name',font=('bold',10))
employeename.place(x=20,y=60)

salary=Label(root,text='salary',font=('bold',10))
salary.place(x=20,y=90)

city=Label(root,text='city',font=('bold',10))
city.place(x=20,y=110)


e_employeeid=Entry()
e_employeeid.place(x=150,y=30)


e_employeename=Entry()
e_employeename.place(x=150,y=60)


e_salary=Entry()
e_salary.place(x=150,y=90)


e_city=Entry()
e_city.place(x=150,y=110)


insert=Button(root,text="insert",font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=150)

delete=Button(root,text="Delete",font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=150)

update=Button(root,text="Update",font=("italic",10),bg="white",command=update)
update.place(x=130,y=150)

get=Button(root,text="Get",font=("italic",10),bg="white",command=get)
get.place(x=190,y=150)


list=Listbox(root)
list.place(x=290,y=30)

show()



root.mainloop()

















