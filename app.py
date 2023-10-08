from tkinter import *
from mysql.connector import connect,Error

def signUp():
    username = ent_user.get()
    password = ent_pass.get()
    ent_user.delete(0,END)
    ent_pass.delete(0,END)
    info = (username,password)
    if username != '' and password != '':
        try:
            with connect(
                host = '127.0.0.1',
                username = 'root',
                passwd = '',
                database = 'tkdb'
                ) as connection:
                insert_query = '''
                                INSERT INTO uandp
                                (username,passwd)
                                VALUES
                                (%s,%s)
                                '''
                with connection.cursor() as mycursor:
                    mycursor.execute(insert_query,info)
                    connection.commit()
                    lbl_wlc.config(text='Your account has been successfully created.')
        except Error as e:
            print(e)
                                      
def signIn():
    def update():        
        old_password = ent_oldpass.get()
        new_password = ent_newpass.get()
        confirm_password = ent_cpass.get()
        ent_oldpass.delete(0,END)
        ent_newpass.delete(0,END)  
        ent_cpass.delete(0,END)
        info = (new_password,username)
        if old_password == password and new_password == confirm_password:
            try:
                with connect(
                        host = '127.0.0.1',
                        username = 'root',
                        passwd = '',
                        database = 'tkdb'
                        ) as connection:
                        update_query = '''
                                    UPDATE uandp
                                    SET passwd = %s
                                    WHERE username = %s
                                    '''
                        with connection.cursor() as mycursor:
                            mycursor.execute(update_query,info)
                            connection.commit()
                            lbl_wlc2.config(text='Your password has been successfully updated.')
            
            except Error as e:
                print(e)
            
    def delete():
        delete_password = ent_dpass.get()
        ent_dpass.delete(0,END) 
        info1 = (username, delete_password) 
        info2 = (username,)
        try:
            with connect(
                    host = '127.0.0.1',
                    username = 'root',
                    passwd = '',
                    database = 'tkdb'
                    ) as connection:
                    select_query = '''
                                    SELECT * FROM uandp WHERE username = %s AND passwd = %s
                                   '''
                    with connection.cursor() as mycursor:
                        mycursor.execute(select_query, info1)
                        data = mycursor.fetchall()
                    try:
                        if delete_password == data[0][1]:
                            delete_query = '''
                                            DELETE FROM uandp WHERE username = %s
                                            '''
                            with connection.cursor() as mycursor:
                                mycursor.execute(delete_query,info2)
                                connection.commit()
                                lbl_wlc3.config(text='Your account has been successfully deleted.')
                    except:
                        lbl_wlc3.config(text='Wrong password! Try again.')
    
        except Error as e:
            print(e)             
  
    username = ent_user.get()
    password = ent_pass.get()
    ent_user.delete(0,END)
    ent_pass.delete(0,END)
    if username != '' and password != '':
        try:
            with connect(
                host = '127.0.0.1',
                username = 'root',
                passwd = '',
                database = 'tkdb'
                ) as connection:
                select_query = '''
                               SELECT * FROM uandp
                               '''
                with connection.cursor() as mycursor:
                    mycursor.execute(select_query)
                    data = mycursor.fetchall()
                    for row in data:
                        if username == row[0] and password == row[1]:
                            win2 = Toplevel(win)
                            win2.title('Profile Setting')
                            win2.geometry('500x500+400+100')
                            lbl_wlc1 = Label(win2,text=f'Welcome {username}')
                            lbl_wlc1.pack()
                            lblf1 = LabelFrame(win2,text='Update',bg='light grey')
                            lblf1.pack(expand='yes',fill='both')
                            
                            lbl_oldpass = Label(lblf1,text='Old Password',bg='light grey')
                            lbl_oldpass.pack()
                            ent_oldpass = Entry(lblf1)
                            ent_oldpass.pack()
                            
                            lbl_newpass = Label(lblf1,text='New Password',bg='light grey')
                            lbl_newpass.pack()
                            ent_newpass = Entry(lblf1)
                            ent_newpass.pack()

                            
                            lbl_cpass = Label(lblf1,text='Confirm Password',bg='light grey')
                            lbl_cpass.pack()
                            ent_cpass = Entry(lblf1)
                            ent_cpass.pack()
                            
                            btn_update = Button(lblf1,text='Update',command=update)
                            btn_update.pack()
                            
                            lbl_wlc2 = Label(lblf1,text='',bg='light grey')
                            lbl_wlc2.pack()
                            
                            lblf2 = LabelFrame(win2,text='Delete',bg='light grey')
                            lblf2.pack(expand='yes',fill='both')
                            
                            lbl_dpass = Label(lblf2,text='Password',bg='light grey')
                            lbl_dpass.pack()
                            ent_dpass = Entry(lblf2)
                            ent_dpass.pack()
                            
                            btn_delete = Button(lblf2,text='Delete',command=delete)
                            btn_delete.pack()
                            
                            lbl_wlc3 = Label(lblf2,text='',bg='light grey')
                            lbl_wlc3.pack()
                            
        except Error as e:
            print(e)  
   
try:
    with connect(
        host = 'localhost',
        username = 'root',
        passwd = ''
        ) as connection:
        create_db = 'CREATE DATABASE IF NOT EXISTS acc'
        create_table = '''CREATE TABLE IF NOT EXISTS uandp
                        (
                           username VARCHAR(20) PRIMARY KEY,
                           passwd VARCHAR(20) NOT NULL
                        )'''
        with connection.cursor() as mycursor:
            mycursor.execute(create_db)
            connection.connect(database = 'tkdb')
            mycursor.execute(create_table)
except Error as e:
    print(e)                            

win = Tk()
win.title('SignUp / SignIn')
win.geometry('500x500+400+100')

lbl_user = Label(win,text='Username')
lbl_user.pack()
ent_user = Entry(win)
ent_user.pack()

lbl_pass = Label(win,text='Password')
lbl_pass.pack()
ent_pass = Entry(win)
ent_pass.pack()

btn_signup = Button(win,text='Sign Up',command=signUp)
btn_signup.pack()
btn_signin = Button(win,text='Sign In',command=signIn)
btn_signin.pack()

lbl_wlc = Label(win,text='')
lbl_wlc.pack()

win.mainloop()