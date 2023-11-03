# -*- coding: utf-8 -*-
"""
password generator with a interface
"""
import customtkinter as ct
import random
import password as pd


ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

root = ct.CTk()
root.geometry("400x250")

def save_on_file_100_pwd():
    """ fname pwd , generate 100 pwd """
    pwd = pd.generate_n_pwd(100)
    with open ("pwd.txt" , mode ="a" , encoding="utf-8") as f:
        for i,n in pwd.items():
            f.write(n)
            f.write("\n") 




frame = ct.CTkFrame(master= root)
frame.pack(pady=20 , padx=20, fill="both", expand = True)

label = ct.CTkLabel(master = frame, text="Password Generator")
label.pack(pady = 10 , padx = 15)
label = ct.CTkLabel(master = frame, text="Every time you click the button\n 100 passwords will generate in a file\ncalled pwd.txt")
label.pack(pady = 10 , padx = 15)

button = ct.CTkButton(master = frame,text="Generate Password" , command= save_on_file_100_pwd)
button.pack(pady = 10 , padx = 15)


root.mainloop()
