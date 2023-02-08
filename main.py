#------------simple text editor ----------------
import os.path
from tkinter import *
from tkinter import colorchooser, font, filedialog, messagebox

def changeFont(*args):
    text_area.config(font=(font_name.get() , font_size.get()))

def changeColor():
    color = colorchooser.askcolor()
    hex_color = color[1]
    text_area.config(fg=hex_color)

#_________ function for Menu Bar___________

def openFile():

    filepath = filedialog.askopenfilename(defaultextension='.txt',
                                          file=[('All files','*.*'),
                                                ('Documents File','*.txt')])

    window.title(os.path.basename(filepath))
    try:
        text_area.delete(1.0,END)
        file = open(filepath,'r')
        text_area.insert(1.0,file.read())

    except Exception:
        print("couldn't read file")
    finally:
        file.close()


def saveFile():
    filepath = filedialog.asksaveasfilename(initialfile="unititled", defaultextension='.txt',
                                        filetypes=[("text file",'*.txt'),
                                                   ("html file",'*.html'),
                                                   ("All files",'*.*')])
    if filepath is None:
        return
    else:
        try:
            window.title(os.path.basename(filepath))
            file = open(filepath,'w')
            text =text_area.get(1.0,END)
            file.write(text)
        except Exception:
            print("couidn't save this file")
        finally:
            file.close()

def newFile():
    window.title("unititled")
    text_area.delete(1.0,END)

def copyFile():
    text_area.event_generate("<<Copy>>")

def pasteFile():
    text_area.event_generate("<<Paste>>")

def cutFile():
    text_area.event_generate("<<Cut>>")

def helpBox():
    messagebox.showinfo("About this programm","this is a simple text editor for my learning python hope it help to you too :)")

#____________Window______________

window = Tk()
window.title("Text Editor")

width_window = 500
hieght_window = 500

filepath = None

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (width_window / 2)) # for position width window should be near midlle
y = int((screen_height / 2) - (hieght_window / 2)) # for position height window should be near midlle

window.geometry('{}x{}+{}+{}'.format(width_window, hieght_window , x, y))

font_name = StringVar(window)
font_name.set('Arial') # set defult font name

font_size = StringVar(window)
font_size.set('20') # set defult font size

text_area = Text(window, font=(font_name.get() , font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + W + S + E)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid(row=1)

change_font = OptionMenu(frame, font_name, *font.families() , command=changeFont)
change_font.grid(row=1,column=0)

size_font = Spinbox(frame, from_=1, to=100, textvariable=font_size , command=changeFont)
size_font.grid(row=1,column=1)

change_color = Button(frame, text="Change Color", command=changeColor)
change_color.grid(row=1,column=2)

menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
edit_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File',menu=file_menu)
menubar.add_cascade(label='Edit',menu=edit_menu)
menubar.add_cascade(label='Help',menu=help_menu)

file_menu.add_command(label='Open', command=openFile)
file_menu.add_command(label='Save', command=saveFile)
file_menu.add_command(label='New', command=newFile)
file_menu.add_separator()
file_menu.add_command(label='Exist',command=quit)

edit_menu.add_command(label='Copy',command=copyFile)
edit_menu.add_command(label='Paste',command=pasteFile)
edit_menu.add_command(label='Cut',command=cutFile)

help_menu.add_command(label='About', command=helpBox)

window.mainloop()