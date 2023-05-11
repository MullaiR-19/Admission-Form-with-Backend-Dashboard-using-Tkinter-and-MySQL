'''Higher Secondry Addmission form'''
#import Necessary Libraries
from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as msgbox
import time

#Clear all Input box after succesful submission of data
def clear_input_text():
    name_t.delete(0,'end')
    paren_name_t.delete(0,'end')
    age_t.delete(0,'end')
    present_address_t.delete(0,'end')
    permanent_address_t.delete(0,'end')
    Relegion_t.delete(0,'end')
    Dob_t.delete(0,'end')
    nationality_t.delete(0,'end')
    sslc_t.delete(0,'end')
    math_t.delete(0,'end')
    sci_t.delete(0,'end')
    mail_t.delete(0,'end')
    num_t.delete(0,'end')
    altnum_t.delete(0,'end')
    gender.set('Select')
    menu.set('Select')

#get data and send to sql database
def submit():        
    #Get data from text box Store in variable
    student_name = name_t.get()
    parent_name = paren_name_t.get()
    age = age_t.get()
    address_r = present_address_t.get()
    address_p = permanent_address_t.get()
    relegion = Relegion_t.get()
    sex = gender.get()
    dob = Dob_t.get()
    nationality = nationality_t.get()
    sslc = sslc_t.get()
    math = math_t.get()
    sci = sci_t.get()
    group_selcted = menu.get()
    mail = mail_t.get()
    number = num_t.get()
    altnumber = altnum_t.get()
    print('Data stored')
    #try to connect to data base and upload data
    try:
        mydb = mysql.connect(host = "localhost",
                             user = "root",
                             passwd = "password",
                             port=3306,
                             database = "admission_record")
        print('Connected to database')
        mycursor = mydb.cursor()
        #formate the data to upload using insert into command
        mycursor.execute("insert into admission_record values('"+student_name+"','"+parent_name+"','"+age+"','"+address_r+"','"+address_p+"','"+relegion+"','"+sex+"','"+dob+"','"+nationality+"','"+sslc+"','"+math+"','"+sci+"','"+group_selcted+"','"+mail+"','"+number+"','"+altnumber+"')")
    
        mycursor.execute("commit")
        msgbox.showinfo(title="Success", message = "Application Recived Succufully!")
        mydb.close()
        #call function to clear input box
        clear_input_text()
    #pitch error message incase of missing data in input or wrong data    
    except:
        msgbox.showinfo(title="Error", message = "Fill in all the data")


#Creating Tk windows
win = Tk()
win.geometry('640x640')
win.resizable(0,1)
win.title("Admission Form-JKF International School")
my_font=('times new roman', 12)

#creating input lables
title = Label(win, text = 'Higher Secondry Admission Form', font=('times new roman', 18)).grid(row=0,column=0,columnspan=2)
name_l = Label(win, text = 'Student Name', font=my_font).grid(row=2,column=0,sticky = W,pady=2)
paren_name_l = Label(win, text = 'Parent Name', font=my_font).grid(row=3,column=0,sticky = W,pady=2)
age_l = Label(win, text = 'Age', font=my_font).grid(row=4,column=0,sticky = W,pady=2)
present_address_l = Label(win, text = 'Present Address', font=my_font).grid(row=5,column=0,sticky = W,pady=2)
permanent_address_l = Label(win, text = 'Permanent Address', font=my_font).grid(row=6,column=0,sticky = W,pady=2)
Relegion_l = Label(win, text = 'Relegion', font=my_font).grid(row=7,column=0,sticky = W,pady=2)
Sex_l = Label(win, text = 'Sex', font=my_font).grid(row=8,column=0,sticky = W,pady=2)
#creating drop down menu for gender selection
gender_list = ['Male','Female','Other']
gender = StringVar()
gender.set('Select')
gender_select =OptionMenu(win, gender, *gender_list)
gender_select.config(font=my_font)
gender_select.grid(row=8,column=1,sticky = W)

Dob_l = Label(win, text = 'Date of Birth', font=my_font).grid(row=9,column=0,sticky = W,pady=2)
nationality_l = Label(win, text = 'Nationality', font=my_font).grid(row=10,column=0,sticky = W,pady=2)
sslc_l = Label(win, text = 'SSLC mark', font=my_font).grid(row=11,column=0,sticky = W,pady=2)
math_l = Label(win, text = 'Maths mark', font=my_font).grid(row=12,column=0,sticky = W,pady=2)
sci_l = Label(win, text = 'Science mark', font=my_font).grid(row=13,column=0,sticky = W,pady=0)
select_grp = Label(win, text='Select Group', font=('times new roman', 12,'bold')).grid(row=14,column=0,sticky = W)
#creating drop down menu for group selection
available_groups = ['Science','Biology','Commers','Business Maths']
menu = StringVar()
menu.set("Select")
group_select = OptionMenu(win, menu, *available_groups)
group_select.config(font=my_font)
group_select.grid(row=14,column=1,sticky=W)

mail_l = Label(win, text = 'E-mail ID', font=my_font).grid(row=19,column=0,sticky = W,pady=5)
num_l = Label(win, text = 'Contact Number', font=my_font).grid(row=20,column=0,sticky = W,pady=5)
altnum_l = Label(win, text = 'Alternative Number', font=my_font).grid(row=21,column=0,sticky = W,pady=5)

#Input textboxes 
name_t = Entry(win, font=my_font)
name_t.grid(row=2,column=1,sticky = W)
paren_name_t = Entry(win, font=my_font)
paren_name_t.grid(row=3,column=1,sticky = W)
age_t = Entry(win,font=my_font)
age_t.grid(row=4,column=1,sticky = W)
present_address_t = Entry(win, font=my_font)
present_address_t.grid(row=5,column=1,sticky = W)
permanent_address_t = Entry(win,font=my_font)
permanent_address_t.grid(row=6,column=1,sticky = W)
Relegion_t = Entry(win, font=my_font)
Relegion_t.grid(row=7,column=1,sticky = W)
Dob_t = Entry(win, font=my_font)
Dob_t.grid(row=9,column=1,sticky = W)
nationality_t = Entry(win, font=my_font)
nationality_t.grid(row=10,column=1,sticky = W)
sslc_t = Entry(win, font=my_font)
sslc_t.grid(row=11,column=1,sticky = W)
math_t = Entry(win, font=my_font)
math_t.grid(row=12,column=1,sticky = W)
sci_t = Entry(win, font=my_font)
sci_t.grid(row=13,column=1,sticky = W)
mail_t = Entry(win, font=my_font)
mail_t.grid(row=19,column=1,sticky = W)
num_t = Entry(win, font=my_font)
num_t.grid(row=20,column=1,sticky = W)
altnum_t = Entry(win,font=my_font)
altnum_t.grid(row=21,column=1,sticky = W)

#one button to over all processes
submit_b = Button(win,text='Submit', font=('times new roman', 14,'bold'),fg='white',bg='#0054e7',command = submit).grid(row=21,column=3,padx=50)

#logo of the school to display in the left
img = PhotoImage(file = 'school-logo.png')
img1 = img.subsample(2, 2)
img_lable = Label(win,image = img1).grid(row=5,column=3,padx=50,rowspan=6)

#Instruction and other data to the applicant
note_t = Label(win, text = '''Last date for submitting form is 00/00/2022
               \n "For late admission contact Admission office in person"''', font=('times new roman', 12,'bold')).grid(row=22,column=1,sticky = W,pady=5,columnspan=6)
address_l = Label(win, text = '  JKF Internation School , Chennai-38, Phone: 044 - 73551934, 85638323').grid(row=23,column=1,sticky = W,pady=5,columnspan=6)
contact_l = Label(win, text = '').grid(row=24,column=1,sticky = W,pady=5,columnspan=6)
win.mainloop()
