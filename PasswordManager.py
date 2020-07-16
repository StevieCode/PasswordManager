from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import PasswordGenerator as PG

# Create a root rk object
root = Tk()
root.title("Password Manager")

# Create a labels
label_acc = Label(root, text = "Account: ").grid(row = 0, sticky = "W")
label_pass = Label(root, text = "Password: ").grid(row = 1, sticky = "W")

# Create account and password entries
acc = Entry(root, width = 35, borderwidth = 5)
e = Entry(root, width = 35, borderwidth = 5)
acc.grid(row = 0, column = 1, columnspan = 3, padx = 5, pady = 5, sticky = "E")
e.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5, sticky = "E")

# Define click button behavior
def GenButton():
    password = PG.GeneratePassword(16)
    e.delete(0, END)
    e.insert(0, password)

    # Copy the generated password to clipboard for convenience
    e.clipboard_clear()
    e.clipboard_append(password)

    ShowHint()

# Define save button behavior
def SaveButton():
    # Error checking
    if acc.get() == '':
        messagebox.showwarning("", "No account entered")
        return

    if e.get() == '':
        messagebox.showwarning("", "No password entered")
        return

    # Get the account name corresponding to the password
    acc_name = simpledialog.askstring("User Name", "What is your app/website name?", parent = root)

    # Save the combination to a file
    f = open("passwords.dat", "a")
    f.write(acc_name + acc.get() + "ä" + e.get())
    f.close()

# Define the load button behavior
def LoadButton():
    try:
        with open("passwords.dat", "r") as file:
            data = file.read()
    except:
        messagebox.showerror("", "Database not found")
        return

    # Ask the user for the account name
    app_name = simpledialog.askstring("User Name", "What is your app/website name?", parent = root)

    # Read the password corresponding to the account name
    found = False
    for i in range(0, len(data) - 16):
        # Find the substring that matches the account name
        substr = data[i : i + len(app_name)]
        if substr == app_name:
            found = True
            # Retrieve the account_name
            k = i + len(app_name)
            while data[k] != 'ä':
                k += 1
            account = data[i + len(app_name) : k]
            password = data[k + 1 : k + 17]

    if not found:
        messagebox.showerror("", "No matched data in the database")
        return

    # Show the retrieved info and copy the password to clipboard
    acc.delete(0, END)
    acc.insert(0, account)
    e.delete(0, END)
    e.insert(0, password)
    e.clipboard_clear()
    e.clipboard_append(password)

    ShowHint()


# Helper function to show the user that the password is copied
def ShowHint():
    hint = Label(root, text = "Password copied!", padx = 5, pady = 5)
    hint.grid(row = 3, column = 0, columnspan = 4)


# Create a button that generates passwords
gen_button = Button(root, text = "Generate a random password", padx = 2, pady = 5, command = lambda: GenButton())

# Create save and load buttons
save_button = Button(root, text = "Save", width = 10, padx = 5, pady = 5, command = lambda: SaveButton())
load_button = Button(root, text = "Load", width = 10, padx = 5, pady = 5, command = lambda: LoadButton())

# Put the buttons on the screen
gen_button.grid(row = 2, column = 0, sticky = "W", columnspan = 3)
load_button.grid(row = 2, column = 1, columnspan = 3)
save_button.grid(row = 2, column = 2, sticky = "E", columnspan = 3)


# Display the gui
root.mainloop()
