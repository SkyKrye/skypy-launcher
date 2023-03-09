#launcher3

import minecraft_launcher_lib
import subprocess
import argparse
import sys
import time
import os

print("""
Welcome to SkyPyLauncher!

""")
#'''
#NEterminal = input("terminal -")

from tkinter import *
import tkinter as tk
from tkinter import CENTER
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("400x300")

w_title = tk.Label(root, text = 'PySky Launcher',  font=('Segoe UI', 50, 'bold'))

bg_image = PhotoImage(file="night.png")
background_label = Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

def create_button(container, text, commandFunction, row, column):
    button = Button(container, text=text, command=root.destroy)
    button.grid(row=row, column=column)

def name_label(container, text, row, column):
    label = Label(container, text=text, bg="SystemButtonFace")
    label.grid(row=row, column=column)

def name_entry(container, row, column):
    entry = Entry(container, textvariable = name_var)
    entry.grid(row=row, column=column)
    
def passw_label(container, text, row, column):
    label = Label(container, text=text, bg="SystemButtonFace")
    label.grid(row=row, column=column)

def passw_entry(container, row, column):
    entry = Entry(container)
    entry.grid(row=row, column=column)

def uuid_label(container, text, row, column):
    label = Label(container, text=text, bg="SystemButtonFace")
    label.grid(row=row, column=column)

def uuid_entry(container, row, column):
    entry = Entry(container)
    entry.grid(row=row, column=column)
    
def token_label(container, text, row, column):
    label = Label(container, text=text, bg="SystemButtonFace")
    label.grid(row=row, column=column)

def token_entry(container, row, column):
    entry = Entry(container)
    entry.grid(row=row, column=column)

container = Frame(root)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

name_var=tk.StringVar()
passw_var=tk.StringVar()
uuid_var=tk.StringVar()
token_var=tk.StringVar()
dir_var=tk.StringVar()

name_label(container, "Username", 0, 2)
name_entry(container, 0, 3)
passw_label(container, "Password", 1, 2)
passw_entry(container, 1, 3)
uuid_label(container, "UUID", 2, 2)
uuid_entry(container, 2, 3)
token_label(container, "Token", 3, 2)
token_entry(container, 3, 3)
create_button(container, "Submit", None, 5, 3)

def submit():
 
    NEusername=name_var.get()
    NEpassword=passw_var.get()
    NEuuid=uuid_var.get()
    NEtoken=token_var.get()
    NEDir=dir_var.get()
     
    print("Username: " + NEusername)
    print("Password: " + NEpassword)
    print("UUID: " + NEuuid)
    print("Token: " + NEtoken)
    print("Directory: " + NEDir)

     
    name_var.set("")
    passw_var.set("")
    uuid_var.set("")
    token_var.set("")
    dir_var.set("")

sub_btn=tk.Button(root,text = 'Submit', command = root.destroy)
root.mainloop()

NEusername=name_var.get()
NEpassword=passw_var.get()
NEuuid=uuid_var.get()
NEtoken=token_var.get()
NEDir=dir_var.get()


#NEpassword = input('Password:')
#masked_password = '*' * len(NEpassword)
#print(f"Your masked password is: {masked_password}")

#NEusername = input("\nYour Mojang username: ")
#NEuuid = input("\nYour Minecraft UUID: ")
#NEtoken = input("\nYour Minecraft token:")

NEDir = "C:\\Users\\Raahim\\OneDrive\\Desktop\\launcher\\.minecraft"

if os.path.exists('save.txt'):
    os.remove('save.txt')
else:
    print('saving content, continuing')
    statsfile=open('save.txt' , 'x')
    statsfile=open('save.txt' , 'w')
    statsfile.write('save-info : \n- username:'+NEusername+'\n- password:'+NEpassword+'\n- UUID:'+NEuuid+'\n- token:'+NEtoken+'\n- directory:'+NEDir)
    statsfile.close()
    print('saved stats to file - save.txt')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", help=NEusername)
    parser.add_argument("--password", help=NEpassword)
#    parser.add_argument("--version", default=minecraft_launcher_lib.utils.get_installed_versions()["release"], help="The Minecraft version")
#    parser.add_argument("--minecraftDir", default=minecraft_launcher_lib.utils.get_minecraft_directory(), help="The path to the Minecraft directory")
    parser.add_argument("--minecraftDir", default=NEDir, help="The path to the Minecraft directory")
    parser.add_argument("--executablePath", help="The path to the java executable")
    parser.add_argument("--jvmArguments", help="The jvm Arguments")
    parser.add_argument("--gameDir", help="Set the game directory")
    parser.add_argument("--demo", action="store_true", help="Run Minecraft in demo mode")
    parser.add_argument("--resolutionWidth", help="Set the resolution width")
    parser.add_argument("--resolutionHeight", help="Set the resolution height")
    parser.add_argument("--server", help="The ip of a server where Minecraft connect to after start")
    parser.add_argument("--port", help="The port of a server where Minecraft connect to after start")
    parser.add_argument("--noInstall", action="store_true", help="Skip Minecraft installation")
    parser.add_argument("--command", action="store_true", help="Print the command and do not run Minecraft")
    args = parser.parse_args().__dict__

    login_data = minecraft_launcher_lib.account.login_user(args["username"], args["password"])
    print('')
    MCuseversion = "1.8.9old"
    #minecraft_directory = args["minecraftDir"]
    minecraft_directory = NEDir
    print("default: " + args["minecraftDir"])
    print("new: " + minecraft_directory)

    # Install specified version
    print('installing version')
#    minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, minecraft_directory)
    print("Starting application", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end=" ")
    time.sleep(1)
    print("Done!")
    print('installed version')
    
#    if "errorMessage" in login_data:
#        print(login_data["errorMessage"])
#        sys.exit(0)

#    if not args["noInstall"]:
#        minecraft_launcher_lib.install.install_minecraft_version(args["version"], args["minecraftDir"], callback={"setStatus": print})

    options = {
        "username": NEusername,
        "uuid": NEuuid,
        "token": NEtoken,
        #"launcherName": "mclauncher-cmd",
        #"launcherVersion": "1.0",
        #"demo": args["demo"],
    }

    if args["executablePath"]:
        options["executablePath"] = args["executablePath"]

    if args["gameDir"]:
        options["gameDirectory"] = args["gameDir"]

    if args["jvmArguments"]:
        options["jvmArguments"] = []
        for i in args["jvmArguments"].split(" "):
            options["jvmArguments"].append(i)

    if args["resolutionWidth"] or args["resolutionHeight"]:
        options["customResolution"] = True
        options["resolutionWidth"] = args["resolutionWidth"] or "854"
        options["resolutionHeight"] = args["resolutionHeight"] or "480"

    if args["server"]:
        options["server"] = args["server"]
        if args["port"]:
            options["port"] = args["port"]
    md = "C:\\Users\\Raahim\\OneDrive\\Desktop\\launcher\\.minecraft"
    command = minecraft_launcher_lib.command.get_minecraft_command(MCuseversion, minecraft_directory, options)

    if args["command"]:
        command_str = ""
        for i in command:
            command_str = command_str + i + " "
        print(command_str[:-1])
        sys.exit(0)

    subprocess.call(command)


if __name__ == "__main__":
    main()
