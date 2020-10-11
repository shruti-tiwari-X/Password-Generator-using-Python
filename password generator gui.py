from tkinter import *
import random
import string
import pyperclip
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator")
Label(root , text = 'Password Generator', font='arial 15 bold').pack()
Label(root, text= 'Shruti Tiwari', font ='arial 10 bold').pack(side= BOTTOM)
pass_str = StringVar()
pass_len=''
def Generator():
    password = ''
    
    for x in range(0,4):
        password = random.choice(string.ascii_uppercase)+ random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
        
    for y in range(pass_len.get()-4):
        password = password + random.choice(string.acii_uppercase +string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()


def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root,text='Copy to Clipboard',command=Copy_password).pack(pady=5)
    
