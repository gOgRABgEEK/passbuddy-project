from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from ttkthemes import ThemedStyle
from PIL import Image,ImageTk
import passgenerator
from pandastable import Table, TableModel
import pandas as pd
import pyperclip            #to copy text on the clipboard.
import openpyxl
import pickle               #to pickle username and password data with dictonary object.
import csv
import os


class loading_win():
    def __init__(self):
        load_win = tk.Tk()
        load_win.title("loading...")
        load_win.configure(bg='#FFFFCC')
        load_win.attributes('-fullscreen','true')

        logo = Image.open(r'G:\PYTHON\GUI\Passbuddy project\passlogo-removebg-preview.png')
        resized_logo = logo.resize((700,280))
        logoimage = ImageTk.PhotoImage(resized_logo)
        imglabel = tk.Label(load_win,image=logoimage,bg='#FFFFCC')
        imglabel.place(x=440,y=170)

        textlabel = tk.Label(load_win,text='At this corner your data is completely safe as only you and your machine is incharge here.\n Data is not on internet it is in your machine so keep it safe with your own way. ',font='"Comic Sans MS" 15 bold',bg='#FFFFCC')
        textlabel.place(x=380,y=450)
        load_win.after(3000,load_win.destroy)
        
        load_win.mainloop()

class security_window():
    def __init__(self):
        global secure_win               
        try:                                     
            if secure_win.state()=='normal':
                secure_win.focus()
        except Exception as e:           
            secure_win = tk.Tk()
            secure_win.title('Security Window')
            secure_win.geometry('1550x900')
            secure_win.configure(bg='#FFFFCC')

            def createpass():
                createpass_win()
                
            # def to_home_window():
            #     home_win = home_window()

            def change_password():
                global ask_win
                def compare():  
                    if(input_entry.get() == password):
                        ask_win.after(10,ask_win.destroy)
                        createpass_win()
                    else:
                        warning_label = tk.Label(ask_win,text='incorrect password',fg='red',font='Arial 12 ')
                        warning_label.place(x=110,y=130)
                        warning_label.after(2000,warning_label.destroy)
                
                #defining asking window for current password.
                try:
                    if ask_win.state() == 'normal':
                        ask_win.focus()
                except Exception as e:
                    ask_win = tk.Tk()
                    ask_win.title('ask window')
                    ask_win.geometry('300x150')
                    ask_win.configure(bg='#FFFFCC')
                    entry_label = tk.Label(ask_win,text='enter current password:',bg='#FFFFCC',font='Arial 10')
                    entry_label.place(x=20,y=55)
                    input_entry = tk.Entry(ask_win)
                    input_entry.place(x=160,y=55) 
                    btn = ttk.Button(ask_win,text='submit',command=compare)
                    btn.place(x=120,y=100)           
            
            def varifier():
                global password
                global username
                u_name = username_entry.get()
                pw = password_entry.get()
                
                war_label = tk.Label(secure_win,bg='#FFFFCC',font='Arial 12')
                war_label.place(x=640,y=600)
                
                if username=='' and password=='':
                    war_label.configure(text="It seems you haven't registered",fg='red')
                    
                elif u_name == username and pw == password:
                    home_window()
                    secure_win.after(1,secure_win.destroy)
                else:
                    war_label.configure(text="Incorrect username or password",fg='red')
                    
            #title
            photo = Image.open(r'G:\PYTHON\GUI\Passbuddy project\lock logo.png')
            resized_photo = photo.resize((150,150))
            img = ImageTk.PhotoImage(resized_photo)
            titlepic_label = tk.Label(secure_win,image=img,bg='#FFFFCC')
            titlepic_label.place(x=530,y=150)
            #title text
            title_text = tk.Label(secure_win,text="Is it you?",bg='#FFFFCC',font='Impact 60')
            title_text.place(x=690,y=180)
            
            #label
            username_label = tk.Label(secure_win,text='Username :',font='"Comic Sans MS" 20 bold',bg='#FFFFCC')
            username_label.place(x=570,y=350)
            #entry
            username_entry = tk.Entry(secure_win,font='"Comic Sans MS" 17 ')
            username_entry.place(x=740,y=355)

            #password label         
            password_label = tk.Label(secure_win,text='Password :',font='"Comic Sans MS" 20 bold',bg='#FFFFCC')
            password_label.place(x=570,y=420)
            #entry
            password_entry = tk.Entry(secure_win,font='"Comic Sans MS" 17 ',show='*')
            password_entry.place(x=740,y=425)

            sub_button = tk.Button(secure_win,text='submit',bg='#FFFFCC',command=varifier,font='Arial 15',width=15)
            sub_button.place(x=700,y=550)

            change_button = tk.Button(secure_win,text='change password',bg='#FFFFCC',font='Arial 15',width=15,command=change_password)
            change_button.place(x=3,y=760)

            if username=='' and password=='':
                button = tk.Button(secure_win,text='first time here?',bg='#FFFFCC',command=createpass,font='15',width=20)
                button.place(x=1280,y=750)
            
            secure_win.mainloop()

class createpass_win:
    def __init__(self):
        global createpass_window
        try:
            if createpass_window.state() == 'normal':
               createpass_window.focus()
        except Exception as e:

            createpass_window = tk.Tk()
            createpass_window.title('create profile')
            createpass_window.geometry('400x400')
            createpass_window.configure(bg='#FFFFCC')
            
            def success():
                global username
                global password

                u_name = user_entry.get()    #stored into global at the register time.           
                p_word = pass_entry.get()    #stored into global at the register time. 
                details = {1:u_name,2:p_word}
                success_label = tk.Label(createpass_window,bg='#FFFFCC',font='Arial 12')
                success_label.place(x=90,y=350)
                
                username = u_name                        #to update username and password on current run.
                password = p_word
                
                if(u_name=='' or p_word == ''):
                    success_label.configure(text='Each field must be filled',fg='red')
                elif(len(p_word) < 6 or len(p_word) > 15):
                    success_label.configure(text='password between 6-15 char',fg='red')
                else:
                    success_label.configure(text='password created successfully',fg='green')
                    createpass_window.after(1500,createpass_window.destroy)
                    
                #To store password and username after closing program. 
                    pickle_out = open(r'G:\PYTHON\GUI\Passbuddy project\keeper.pickle','wb')
                    pickle.dump(details,pickle_out)
                    pickle_out.close()
        
            title_label = tk.Label(createpass_window,text='Register',font='Impact 30 ',bg='#FFFFCC')
            title_label.place(x=120,y=50)

            #username      
            user_label = tk.Label(createpass_window,text='Enter username :',font='"Comic Sans MS" 15',bg='#FFFFCC')
            user_label.place(x=50,y=150)
            user_entry = tk.Entry(createpass_window,width=22) 
            user_entry.place(x=230,y=160)
            #password
            pass_label = tk.Label(createpass_window,text='Create Password :',font='"Comic Sans MS" 15',bg='#FFFFCC')
            pass_label.place(x=50,y=200)
            pass_entry = tk.Entry(createpass_window,width=22,show='*') 
            pass_entry.place(x=230,y=210)

            button = tk.Button(createpass_window,text='submit',bg='#FFFFCC',font='"Comic Sans MS" 13',width=8,command=success)
            button.place(x=160,y=280)

            createpass_window.mainloop()
    
class home_window():
    def __init__(self):
        global home_win
        try:
            if home_win.state()=='normal':
                home_win.focus()
        except Exception as e:
            home_win = tk.Toplevel()
            home_win.title('Home')
            home_win.geometry('1550x900')
            home_win.configure(bg='#FFFFCC')

            logo = Image.open(r'G:\PYTHON\GUI\Passbuddy project\passlogo-removebg-preview.png')
            resized_logo = logo.resize((400,130))
            logoimage = ImageTk.PhotoImage(resized_logo)
            imglabel = tk.Label(home_win,image=logoimage,bg='#FFFFCC')
            imglabel.place(x=540,y=50)

            titletext_label = tk.Label(home_win,text='Welcome to passbuddy! Here you can genereate password according to your need\nand you can store existing password with platform related details and store it your place',
                                    font='"Comic Sans MS" 16 ',bg='#FFFFCC')
            titletext_label.place(x=320,y=160)
            style = ThemedStyle(home_win)
            style.set_theme("aquativo")

            def generatefun():
            #home_window.after(10,home_window.destroy)
                generatepass_win()

            def storefun():
                #home_window.after(10,home_window.destroy)
                store_data()

            #Buttons
            photoimg = Image.open(r'G:\PYTHON\GUI\Passbuddy project\generatepass btn.png')
            photo1 = ImageTk.PhotoImage(photoimg.resize((300,80)))
            generate_button = tk.Button(home_win,image=photo1,bd=0,bg='#FFFFCC',command=generatefun,activebackground='#FFFFCC')
            generate_button.place(x=585,y=325)
            
            photo2img = Image.open(r'G:\PYTHON\GUI\Passbuddy project\save password btn.png')
            photo2 = ImageTk.PhotoImage(photo2img.resize((300,80)))
            save_button = tk.Button(home_win,image=photo2,bd=0,bg='#FFFFCC',command=storefun,activebackground='#FFFFCC')
            save_button.place(x=585,y=410)
            home_win.mainloop()

class generatepass_win:
    def __init__(self):
        global generate_win
        try:
            if generate_win.state() == 'normal':
                generate_win.focus()
        except Exception as e:   
            generate_win = tk.Tk()
            generate_win.title('Generate Password')
            generate_win.geometry('1550x900')
            generate_win.configure(bg = '#FFFFCC')

            def generate_it():
                length = entry.get()
                strength= var.get()
                try:
                    insert_entry.delete(0,tk.END)
                except Exception as e:
                    pass
                insert_entry.insert(1,passgenerator.password_generator(int(length),int(strength)))
                
            def copy():
                pyperclip.copy(insert_entry.get())
                copylabel = tk.Label(frame,text='text copied',font='Arial 13',fg='green')
                copylabel.place(x=160,y=240)
                copylabel.after(3000,copylabel.destroy)

            def tohome():
                # home_window()
                generate_win.after(1,generate_win.destroy)

                
            frame = tk.Frame(generate_win,height=350,width=430,bd=3,)
            frame.place(x=520,y=120)

            label = tk.Label(generate_win,text='choose properties of password you need',font='Arial 12 underline',bg='#FFFFCC')
            label.place(x=513,y=88)

            label2 = tk.Label(frame,text='Number of total character:',font='Arial 11 ')
            label2.place(x=10,y=25)

            entry = tk.Entry(frame,width=5,bg='#FFFFCC')
            entry.place(x=200,y=28)

            #radiobuttons.
            var = tk.IntVar(generate_win)
            rbtn1 = ttk.Radiobutton(frame,text='simple',value=0,variable=var)
            rbtn1.place(x=8,y=80)
            rbtn2 = ttk.Radiobutton(frame,text='medium',value=1,variable=var)
            rbtn2.place(x=158,y=80)
            rbtn3 = ttk.Radiobutton(frame,text='strong',value=2,variable=var)
            rbtn3.place(x=316,y=80)
            
            s = Style()
            s.configure('my.TButton',font='Arial 39 bold')
            #Button
            btn = ttk.Button(frame,text='Generate',style='my.TButton',command=generate_it)
            btn.place(x=160,y=120)

            label3 = tk.Label(frame,text='your password is here',font='Arial 12')
            label3.place(x=140,y=180)
            
            insert_entry = tk.Entry(frame,width=30,bg='#FFFFCC',font='Arial 12')
            insert_entry.place(x=60,y=210)
            
            button = ttk.Button(frame,text='copy',command=copy,width=7)
            button.place(x=312,y=209)   
            backbtn = tk.Button(generate_win,text="BACK",activebackground='red',font='Arial 12 bold',bg='orange',command=tohome)
            backbtn.place(x=10,y=10)
            
            generate_win.mainloop()

class store_data:
    def __init__(self):
        global store_win
        try:
            if store_win.state() == 'normal':
               store_win.focus()
        except Exception as e:
            store_win = tk.Tk()
            store_win.title('storedata window')
            store_win.geometry('1550x900')
            store_win.configure(bg='#FFFFCC')

            def add_details():

                platform = platform_entry.get()
                user__name = uname_entry.get()
                p__word = pass_entry.get()
                email = email_entry.get()
                
                new_row = [platform,user__name,p__word,email]
                # to append all details into already existing csv file.
                with open(r'G:\PYTHON\GUI\Passbuddy project\webinfo.csv','a+',newline='') as f:
                    written = csv.writer(f)
                    written.writerow(new_row)
                
                #deleteing details in entrybox after button click.
                platform_entry.delete(0,tk.END)
                uname_entry.delete(0,tk.END)
                pass_entry.delete(0,tk.END)
                email_entry.delete(0,tk.END)

            def show_table():
                try:
                    try:
                        if root.state() == 'normal':
                           root.focus()
                    except Exception as e:
                        root = tk.Toplevel()
                        root.title("Show Table")
                        root.geometry('800x500')
                        root.configure(bg='#FFFFCC')
                        frame = tk.Frame(root)
                        frame.pack(fill=BOTH)
                        table = Table(frame,showstatusbar=True,showtoolbar=True)
                        table.importCSV(filename=r'G:\PYTHON\GUI\Passbuddy project\webinfo.csv')
                        table.show()
                    
                except Exception as e:
                    permanent_row = ['Platformname','Username','Password','Email']
                    f = open(r'G:\PYTHON\GUI\Passbuddy project\webinfo.csv','a')
                    write = csv.writer(f)
                    write.writerow(permanent_row)
                    f.close()
            def tohome():
                store_win.after(1,store_win.destroy)
            
            def clearlist():
                permanent_row = ['Platformname','Username','Password','Email']
                f = open(r'G:\PYTHON\GUI\Passbuddy project\webinfo.csv','w')
                f.truncate()
                written = csv.writer(f)
                written.writerow(permanent_row)
                f.close()

            platform_label = tk.Label(store_win,text='Enter platformname:',font='Arial 14 bold',bg='#FFFFCC')
            platform_label.place(x=540,y=130)
            platform_entry = tk.Entry(store_win,font='Arial 14 ',width=30)
            platform_entry.place(x=740,y=130)
            platform_entry.focus()

            uname_label = tk.Label(store_win,text='Enter username:',font='Arial 14 bold',bg='#FFFFCC')
            uname_label.place(x=540,y=190)
            uname_entry = tk.Entry(store_win,font='Arial 14 ',width=30)
            uname_entry.place(x=740,y=190)
            
            pass_label = tk.Label(store_win,text='Enter password:',font='Arial 14 bold',bg='#FFFFCC')
            pass_label.place(x=540,y=250)
            pass_entry = tk.Entry(store_win,font='Arial 14 ',width=30)
            pass_entry.place(x=740,y=250)
            
            email_label = tk.Label(store_win,text='Enter email:',font='Arial 14 bold',bg='#FFFFCC')
            email_label.place(x=540,y=310)
            email_entry = tk.Entry(store_win,font='Arial 14 ',width=30)
            email_entry.place(x=740,y=310)
            
            add_btn = tk.Button(store_win,text='ADD',font='Arial 14 bold',activebackground='red',bg='#FFFFCC',command=add_details)
            add_btn.place(x=790,y=400)
            
            show_btn = tk.Button(store_win,text='Show list',font='Arial 14 bold',activebackground='red',bg='#FFFFCC',command=show_table)
            show_btn.place(x=650,y=700)
            
            clear_button = tk.Button(store_win,text='Clear list',font='Arial 14 bold',activebackground='red',bg='#FFFFCC',command=clearlist,)
            clear_button.place(x=780,y=700)

            backbtn = tk.Button(store_win,text="BACK",activebackground='red',font='Arial 12 bold',bg='orange',command=tohome)
            backbtn.place(x=10,y=10)
            store_win.mainloop()


#global windows
secure_win=None
createpass_window=None 
generate_win=None
store_win=None
home_win=None 
root=None         #window to show table.       

#globals
username=''
password=''

new_list={}
 # to read data from file.
# new_list[1] = ''
# new_list[2] = ''
try:
    pickle_in = open(r'G:\PYTHON\GUI\Passbuddy project\keeper.pickle','rb')
    new_list = pickle.load(pickle_in)
    pickle_in.close()
    username=new_list[1]
    password=new_list[2]
except Exception as e:
    pass
   

loading_win()           #object of load window
security_window()

