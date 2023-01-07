from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for one in range(randint(8, 10))]+[choice(symbols) for one in range(randint(2, 4))]+[choice(numbers) for one in range(randint(2, 4))]

    shuffle(password_list)

    passwordd="".join(password_list)
    password_entry.insert(0,passwordd)
    pyperclip.copy(passwordd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    website_name = we.get()
    email_username = email_entry.get()
    new_data={website_name:{"email":email_username,"password":password}}
    if len(password)==0 or len(website_name)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json","r") as data_file:
                data=json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json","w") as data_file:
                 json.dump(new_data,data_file,indent=4)
        else:
            with open("passwords.json","w") as data_file:
                 json.dump(data,data_file,indent=4)
        finally:
            password_entry.delete(0, END)
            we.delete(0, END)
#------------------------ FIND PASSWORD ------------------------------- #
def find_password():
    website=we.get()
    try:
        with open("passwords.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"email: {data[website]['email']}\npassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Opps",message="The website doesn't exist.")




# ---------------------------- UI SETUP ------------------------------- #





window=Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#website label
website=Label(text="Website:")
website.grid(row=1,column=0)

#website entry
we=Entry(width=20)
we.grid(row=1,column=1)
we.focus()    #get the curser at there

#Email/Username label
EU=Label(text="Email/Username:")
EU.grid(row=2,column=0)

#email entry
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"runwang@ucsd.edu")    #insert the email before the user put anything

#Password Label
password=Label(text="Password: ")
password.grid(row=3,column=0)

#Password Entry
password_entry=Entry(width=19)
password_entry.grid(row=3,column=1)

#Password Generator Button
generate_password_button=Button(text="Generate Password",width=12,command=generate_password)
generate_password_button.grid(row=3,column=2)

#Add Button
add_button=Button(width=34,text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2)

#Search Button
search=Button(text="Search",width=12,command=find_password)
search.grid(row=1,column=2)

window.mainloop()


#json.dump() put info into json
#json.load() read info in json
#json.update()