from mysql import connector as mysql
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Admission Records")
win.geometry('720x640')
win.resizable(1,1)
label = Label(win, text="Student Data", font=("Arial",30)).place(relx=0.01,rely=0.01,height=30,width=1280)

scrollX = Scrollbar(win, orient=HORIZONTAL)
scrollY = Scrollbar(win, orient=VERTICAL)

columns = ('Name', 'Parent Name', 'Age','Present Address', 'Permanent Address', 'Relegion', 'Sex', 'DOB', 'Nationality', 'SSLC Mark', 'Maths Mark', 'Science Mark', 'Group', 'Mail ID', 'Number', 'Alt Number')

listBox = ttk.Treeview(win, columns=columns, show='headings')
listBox.config(xscrollcommand=scrollX.set)
listBox.config(yscrollcommand=scrollY.set)
listBox.config(selectmode='extended')

scrollX.config(command=listBox.xview)
scrollX.place(relx=0.01,rely=0.97,height=15,width=1260)

scrollY.config(command=listBox.yview)
scrollY.place(relx=0.95,rely=0.06,height=650,width=15)

for col in columns:
    listBox.heading(col, text=col)    
    listBox.place(relx=0.005, rely=0.06, height=650,width=1260)
#closeButton = Button(win, text="Close", width=15, command=exit).grid(row=4, column=1)

try:
    mydb = mysql.connect(host = "localhost",
                             user = "root",
                             passwd = "password",
                             port=3306,
                             database = "admission_record")
    
    mycursor = mydb.cursor()    
    query="select * from admission_record;"    
    mycursor.execute(query)    
    data_in_database=mycursor.fetchall()

    for i, (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p) in enumerate(data_in_database, start=1):
            listBox.insert("", "end", values=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p))
            mycursor.close()

    
    '''# print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()'''
    

except Exception as e:
    print(e)
win.mainloop()
