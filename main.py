from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
#import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    #pyperclip.copy(password)

    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email":  email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        empty = messagebox.showinfo(title="Empty fields", message="Hey! don't leave any fields empty.")
    else:
        try:
            with open("data.txt", "r") as data_file:
                # data = json.load(data_file)
                data = data_file.read()

        except FileNotFoundError:
            with open("data.txt", "w") as data_file:
                #json.dump(new_data, data_file, indent=4)
                data_file.write(new_data)
        else:
            #data.update(new_data)
            data = new_data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
#canvas.pack()

website_label = Label(text="Website:", font=("Ariel", 12))
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:", font=("Ariel", 12))
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "estherojinji@gmail.com")

password_label = Label(text="Password:", font=("Ariel", 12))
password_label.grid(row=3, column=0)

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=gen_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=31, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()