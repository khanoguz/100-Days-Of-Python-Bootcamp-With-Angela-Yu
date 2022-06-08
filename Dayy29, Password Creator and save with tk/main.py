from tkinter import  *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password():
    password_textbox.delete(0,END)
    password_list = []

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = password_list + [random.choice(letters) for xx in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for xx in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for xx in range(nr_numbers)]

    random.shuffle(password_list)
    password_txt = ""
    for i in password_list:
        password_txt += i

    password_textbox.insert(0, password_txt)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()

    text = f"{website} | {email} | {password}\n"

    if website == "":
        messagebox.showwarning(title="Warning", message="Please insert an e-mail")
    elif password == "":
        messagebox.showwarning(title="Warning", message="Please insert a password")
    else:
        control = messagebox.askokcancel(title="Control", message=f"website:{website}\nemail:{email}\npassword:{password}")
        if control:
            with open("data.txt","a") as f:
                f.write(text)
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)

            messagebox.showinfo(title="Info", message="Added!")
        else:
            pass
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column= 1, row= 0)


website_label = Label(text="Website:", font=("Courier", 15, "bold"))
website_label.grid(column=0,row=1)

website_textbox = Entry(width=35)
website_textbox.grid(column=1,row=1, columnspan=2,sticky=EW)
website_textbox.focus()

email_label = Label(text="Email/Username:", font=("Courier", 15, "bold"))
email_label.grid(column=0, row=2)

email_textbox = Entry(width=35)
email_textbox.grid(column=1, row=2, columnspan=2,sticky=EW)
email_textbox.insert(0, "oguzkaganbilici1@gmail.com")
password_label = Label(text="Password:", font=("Courier",15,"bold"))
password_label.grid(column=0,row=3)

password_textbox = Entry(width=21)
password_textbox.grid(column=1,row=3,sticky=EW)

generate_password = Button(text="Generate Password",command=random_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width= 36, command= save)
add_button.grid(column=1, row=4, columnspan=2,sticky=EW)

window.mainloop()