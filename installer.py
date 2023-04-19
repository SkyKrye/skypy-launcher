#installer

import subprocess
import time

subprocess.run(["pip", "install", "minecraft-launcher-lib"])
subprocess.run(["pip", "install", "argparse"])
subprocess.run(["pip", "install", "tkinter"])
subprocess.run(["pip", "list"])
time.sleep(10)

print('Installation done!')
print("A messagebox should show up for you on screen, if it doesn't, then that means that tkinter was configured incorrectly")

from tkinter import *
from tkinter import messagebox

messagebox.showinfo("skypy-launcher", """The following modules have been installed successfully:
> minecraft-launcher-lib
> argparse
> tkinter""")
