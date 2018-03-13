from tkinter import *
from view import *
from tkinter.messagebox import *
class Mainpage(object):
    def __init__(self,master=None):
        self.root=master
        self.root.geometry('600x500')
        self.createPage()
    def createPage(self):
        self.addinfo=add(self.root)
        self.queryinfo=query(self.root)
        self.addinfo.pack()
        menubar=Menu(self.root)
        menubar.add_command(label='添加',command=self.add_info)
        menubar.add_command(label='查询',command=self.query_info)
        self.root['menu']=menubar

    def add_info(self):
        self.queryinfo.pack_forget()
        self.addinfo.pack()
    def query_info(self):
        self.addinfo.pack_forget()
        self.queryinfo.pack()
        
        
