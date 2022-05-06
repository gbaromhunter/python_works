#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Mar 04, 2022 09:18:35 PM EET  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import password_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("552x285+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top
        self.password = tk.StringVar()
        self.tch49 = tk.IntVar()
        self.tch52 = tk.IntVar()

        self.frame_principale = ttk.Frame(self.top)
        self.frame_principale.place(relx=0.016, rely=0.067, relheight=0.902
                , relwidth=0.976)
        self.frame_principale.configure(relief='groove')
        self.frame_principale.configure(borderwidth="2")
        self.frame_principale.configure(relief="groove")

        self.entry_password = ttk.Entry(self.frame_principale)
        self.entry_password.place(relx=0.05, rely=0.074, relheight=0.16
                , relwidth=0.902)
        self.entry_password.configure(textvariable=self.password)
        self.entry_password.configure(takefocus="")
        self.entry_password.configure(cursor="ibeam")

        self.button_generate = ttk.Button(self.frame_principale)
        self.button_generate.place(relx=0.241, rely=0.272, height=55, width=126)
        self.button_generate.configure(takefocus="")
        self.button_generate.configure(text='''Genera!''')
        self.button_generate.configure(compound='left')
        self.button_generate.configure(command= lambda )

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.check_numbers = ttk.Checkbutton(self.frame_principale)
        self.check_numbers.place(relx=0.482, rely=0.311, relwidth=0.16
                , relheight=0.0, height=23)
        self.check_numbers.configure(variable=self.tch49)
        self.check_numbers.configure(takefocus="")
        self.check_numbers.configure(text='''Numeri''')
        self.check_numbers.configure(compound='left')

        self.char_number = ttk.Spinbox(self.frame_principale, from_=1, to=100)
        self.char_number.place(relx=0.501, rely=0.545, relheight=0.101
                , relwidth=0.178)
        self.char_number.configure(background="white")
        self.char_number.configure(takefocus="")

        self.check_special = ttk.Checkbutton(self.frame_principale)
        self.check_special.place(relx=0.482, rely=0.428, relwidth=0.223
                , relheight=0.0, height=21)
        self.check_special.configure(variable=self.tch52)
        self.check_special.configure(takefocus="")
        self.check_special.configure(text='''Caratteri speciali''')
        self.check_special.configure(compound='left')

        self.laber_char = ttk.Label(self.frame_principale)
        self.laber_char.place(relx=0.297, rely=0.506, height=39, width=105)
        self.laber_char.configure(background="#d9d9d9")
        self.laber_char.configure(foreground="#000000")
        self.laber_char.configure(font="TkDefaultFont")
        self.laber_char.configure(relief="flat")
        self.laber_char.configure(anchor='w')
        self.laber_char.configure(justify='left')
        self.laber_char.configure(text='''Numero caratteri''')
        self.laber_char.configure(compound='left')

def start_up():
    password_support.main()

if __name__ == '__main__':
    password_support.main()




