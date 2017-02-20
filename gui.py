from tkinter import *
from tkinter import ttk


txt = ''


class Login(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lb_user = Label(self, text='Username').grid(column=0, row=0, sticky=E)
        # self.lb_user.pack()

        self.entry_user = Entry(self).grid(column=1, row=0, padx=10)
        # self.entry_user.pack()

        self.lb_password = Label(self, text='Password').grid(column=0, row=1, sticky=E)
        # self.lb_password.pack()

        self.entry_password = ttk.Entry(self, show='*', textvariable=txt).grid(column=1, row=1, padx=10)
        # self.entry_password.pack()

        self.bu_check = Button(self, text='Check', command=self.on_bu_check).grid(column=0, row=2)
        # self.bu_check.pack()

    def on_bu_check(self):
        # self.entry_user.text
        # print('Password: ', self.entry_password.get())
        print('Password: ', txt)
        # print('User    : ', self.entry_user.get())


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text='button1')
        self.button1.pack(side='left')

        self.button2 = Button(self, text='buttton2')
        self.button2.pack(side='left')

        self.button3 = Button(self, text='button3')
        self.button3.pack(side='left')

        self.button4 = Button(self, text='button4')
        self.button4.pack(side='left', padx=5, pady=8, fill='none')

        self.quit = Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side='left')

root = Tk()
# app = Application(master=root)
app = Login(master=root)
app.mainloop()
