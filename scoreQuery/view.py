from tkinter import *
import pymysql
from tkinter.messagebox import *


class add(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_add(self,name,subject,score):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='info',charset='utf8')
        cursor=conn.cursor()
        name=name.get()
        subject=subject.get()
        score=score.get()
        sql="insert into score(name,subject,score) values('%s','%s','%s') "%(name,subject,score)
        flag=cursor.execute(sql)
        conn.commit()
        if(flag==1):
            showinfo(message="添加数据成功")
        else:
            showinfo(message="添加数据失败")
        cursor.close()
        conn.close()
        
    def createPage(self):
        Label(self,text="姓名:").pack()
        name=Entry(self)
        name.pack()
        Label(self,text="科目:").pack()
        subject=Entry(self)
        subject.pack()
        Label(self,text="成绩:").pack()
        score=Entry(self)
        score.pack()
        button=Button(self,text="添加", command=lambda:self.db_add(name,subject,score))
        button.pack()

        
class query(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_query(self,name):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='info',charset='utf8')
        cursor=conn.cursor()
        name=name.get()
        sql="select subject,score from score where name= '%s'"%(name)
        result=cursor.execute(sql)
        row=cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if(result==0):
            showinfo(message="数据库中无此数据")
        else:
            var1=StringVar()
            label0=Label(self,textvariable=var1)
            label0.pack()
            var1.set(name)
            for j in range(result):
                if j>=10:
                    break;
                var=StringVar()
                label=Label(self,textvariable=var)
                label.pack()
                str="科目   "+row[j][0]+"         成绩   "+row[j][1]
                var.set(str)
                
        
    def createPage(self):
        Label(self,text='姓名：').pack()
        name=Entry(self)
        name.pack()
        button=Button(self,text='查询',command=lambda:self.db_query(name))
        button.pack()
        
    
