#Модули
from tkinter import *
from tkinter import messagebox
import shutil
import subprocess
import getpass
import os


#Окно программы
root = Tk()
root.title("WallEngine")
root.geometry("260x380")
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")


#Фон программы
photo = PhotoImage(file="bg.png")
label = Label(image=photo)
label.pack()


#Пользователь и пути
USER_NAME = getpass.getuser()
path1 = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
path2 = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autorun.lnk" % USER_NAME


#Меню
def autorun_on():
    if os.path.exists(path2):
        messagebox.showwarning("WallEngine", "Autorun is already enabled.")
    else:
        messagebox.showinfo("WallEngine", "Autorun is enabled.")
        shutil.copy("launch_muted.lnk", path1)

def autorun_off():
    if os.path.exists(path2):
    	messagebox.showinfo("WallEngine", "Autorun is disabled.")
    	os.remove(path2)
    else:	
        messagebox.showwarning("WallEngine", "Autorun is not enabled.")
        
def wallpaper_folder():
	if os.path.exists("Wallpaper"):
		subprocess.Popen('explorer "Wallpaper"') 
	else:
	    messagebox.showerror("Error", "Folder not found!")	

def about():
    messagebox.showinfo("About", "Version 1.8 - Code written by MasajiNobe")  

menu_bar = Menu()

autorun_menu = Menu(tearoff=0)
autorun_menu.add_command(label="Enabled", command=autorun_on)
autorun_menu.add_command(label="Disabled", command=autorun_off)

menu_bar.add_cascade(label="Autorun", menu=autorun_menu)
menu_bar.add_cascade(label="Wallpaper", command=wallpaper_folder)
menu_bar.add_cascade(label="About", command=about)


#GUI
def launch():
    os.startfile("launch.vbs")
    btn_launch['state'] = 'disabled'

def launch_muted():
    os.startfile("launch_muted.vbs")
    btn_launch_muted['state'] = 'disabled'

def skip():
    os.startfile("skip.lnk")

def pause_resume():
    os.startfile("pause_resume.lnk")

def stop():
    os.startfile("stop.lnk")
    btn_launch['state'] = 'normal'
    btn_launch_muted['state'] = 'normal'
       
btn_launch = Button(
text="Launch", 
 padx="14", 
  pady="7", 
   background="#16597E", 
    foreground="#ffffff", 
     activebackground="#ffffff", 
      activeforeground="#16597E", 
       font="Tahoma 12 bold", 
        command=launch)

btn_launch.place(
relx=.5, 
 rely=.08, 
  anchor="c", 
   height=30, 
    width=150, 
     bordermode=OUTSIDE)

btn_launch_muted = Button( 
text="Launch(muted)", 
 padx="14", 
  pady="7", 
   background="#16597E", 
    foreground="#ffffff", 
     activebackground="#ffffff", 
      activeforeground="#16597E", 
       font="Tahoma 12 bold", 
        command=launch_muted) 

btn_launch_muted.place( 
 relx=.5, 
  rely=.24, 
   anchor="c", 
    height=30, 
     width=150, 
      bordermode=OUTSIDE)

btn_skip = Button(
text="Skip",
 padx="14",
  pady="7",
   background="#16597E",
    foreground="#ffffff",
     activebackground="#ffffff",
      activeforeground="#16597E",
       font="Tahoma 12 bold",
        command=skip)

btn_skip.place(
relx=.5,
 rely=.56,
  anchor="c",
   height=30,
    width=150,
     bordermode=OUTSIDE)

btn_pause_resume = Button(
text="Pause/Resume", 
 padx="14", 
  pady="7", 
   background="#16597E", 
    foreground="#ffffff", 
     activebackground="#ffffff", 
      activeforeground="#16597E", 
	   font="Tahoma 12 bold",
	    command=pause_resume)

btn_pause_resume.place(
relx=.5,
 rely=.72, 
  anchor="c",
   height=30,
    width=150,
     bordermode=OUTSIDE)

btn_stop = Button(
text="Stop",
 padx="14", pady="7",
  background="#16597E",
   foreground="#ffffff",
    activebackground="#ffffff",
     activeforeground="#16597E",
      font="Tahoma 12 bold",
       command=stop)

btn_stop.place(
relx=.5,
 rely=.88, 
  anchor="c",
   height=30,
    width=150,
     bordermode=OUTSIDE)


root.config(menu=menu_bar)
root.mainloop()