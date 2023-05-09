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
  
root=tk.Tk()
 

bg_image = tk.PhotoImage(file="night.png")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)
root.minsize(400, 500)
root.geometry('1000x700')

name_var=tk.StringVar()
passw_var=tk.StringVar()
uuid_var=tk.StringVar()
token_var=tk.StringVar()
dir_var=tk.StringVar()

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

container = Frame(root, bg="#1b3035", highlightthickness=10, highlightbackground="#1b3035")
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def create_title(container, text, row, column):
    label = Label(container, text=text, bg="#1b3035", fg="white", font=('Segoe UI', 20, 'bold'))
    label.grid(row=row, column=column)

container2 = Frame(root, bg="#1b3035", highlightthickness=10, highlightbackground="#1b3035")
container2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
create_title(container2, "SkyPyCraft Launcher", 0, 0)

#name
name_label = tk.Label(container, text = 'Username', font=('calibre',10, 'bold'), bg="#1b3035", fg="white")
name_entry = tk.Entry(container,textvariable = name_var, font=('calibre',10,'normal'), bg="#1b3035", fg="white")
name_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
  
#password
passw_label = tk.Label(container, text = 'Password', font = ('calibre',10,'bold'), bg="#1b3035", fg="white")
passw_entry=tk.Entry(container, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*', bg="#1b3035", fg="white")
passw_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

#UUID
uuid_label = tk.Label(container, text = 'UUID', font=('calibre',10, 'bold'), bg="#1b3035", fg="white")

#UUID
uuid_entry = tk.Entry(container,textvariable = uuid_var, font=('calibre',10,'normal'), bg="#1b3035", fg="white")

#Token
token_label = tk.Label(container, text = 'Token', font = ('calibre',10,'bold'), bg="#1b3035", fg="white")
token_label.place(relx=0.5, rely=0.8, anchor=CENTER)

#Token
token_entry=tk.Entry(container, textvariable = token_var, font = ('calibre',10,'normal'), show = '*', bg="#1b3035", fg="white")
token_entry.place(relx=0.6, rely=0.8, anchor=CENTER)

#Directory
dir_label = tk.Label(container, text = 'Directory', font = ('calibre',10,'bold'), bg="#1b3035", fg="white")
dir_entry=tk.Entry(container, textvariable = dir_var, font = ('calibre',10,'normal'), bg="#1b3035", fg="white")

w_label = tk.Label(container, text = 'Version', font = ('calibre',10,'bold'), bg="#1b3035", fg="white")
variable = StringVar(container)
variable.set("select version") # default value
w = OptionMenu(container, variable, "1.8.9", "1.16.5", "1.19.3")
w.config(width=17, bg="#1b3035", fg="white", activebackground="#1b3035", activeforeground="white", highlightbackground="#1b3035")
w["menu"].config(bg="#1b3035", fg="white", activeforeground="white")
sub_btn=tk.Button(container,text = 'Submit', command = root.destroy, bg="#1b3035", fg="white")

name_label.grid(row=0,column=2)
name_entry.grid(row=0,column=3)
passw_label.grid(row=1,column=2)
passw_entry.grid(row=1,column=3)
uuid_label.grid(row=2,column=2)
uuid_entry.grid(row=2,column=3)
token_label.grid(row=3,column=2)
token_entry.grid(row=3,column=3)
dir_label.grid(row=4,column=2)
dir_entry.grid(row=4,column=3)
w_label.grid(row=5, column=2)
w.grid(row=5, column=3)
sub_btn.grid(row=7,column=3)

root.mainloop()

NEusername=name_var.get()
NEpassword=passw_var.get()
NEuuid=uuid_var.get()
NEtoken=token_var.get()
NEDir=dir_var.get()
MCuseversion=variable.get()

if MCuseversion == 'select version':
    MCuseversion = '1.8.9'

if NEusername and NEpassword:
    pass
else:
    print('at least 2 variables required')
    sys.exit()

#NEpassword = input('Password:')
#masked_password = '*' * len(NEpassword)
#print(f"Your masked password is: {masked_password}")

#NEusername = input("\nYour Mojang username: ")
#NEuuid = input("\nYour Minecraft UUID: ")
#NEtoken = input("\nYour Minecraft token:")

appdata = os.getenv('APPDATA')
NEDir = appdata+'\\.minecraft'

if os.path.exists('save.txt'):
    os.remove('save.txt')
    statsfile=open('save.txt' , 'x')
    statsfile=open('save.txt' , 'w')
    statsfile.write('save-info : \n- username:'+NEusername+'\n- password:'+NEpassword+'\n- UUID:'+NEuuid+'\n- token:'+NEtoken+'\n- directory:'+NEDir+'\n- version:'+MCuseversion)
    statsfile.close()
    print('saved stats to file - save.txt')

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
#    MCuseversion = "1.8.9"
    #minecraft_directory = args["minecraftDir"]
    minecraft_directory = NEDir
    print("default: " + args["minecraftDir"])
    print("new: " + minecraft_directory)

    if MCuseversion == '1.8.9':
        if os.path.exists(NEDir+'\\versions\\1.8.9'):
            pass
            #minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, minecraft_directory)
        else:
            minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, NEDir)

    if MCuseversion == '1.16.5':
        if os.path.exists(NEDir+'\\versions\\1.16.5'):
            pass
            #minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, minecraft_directory)
        else:
            minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, NEDir)

    if MCuseversion == '1.19.3':
        if os.path.exists(NEDir+'\\versions\\1.19.3'):
            pass
            #minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, minecraft_directory)
        else:
            minecraft_launcher_lib.install.install_minecraft_version(MCuseversion, NEDir)

    # Install specified version
    print('installing version')
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
        "launcherName": "mclauncher-cmd",
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
    md = "%appdata%\\.minecraft"
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
