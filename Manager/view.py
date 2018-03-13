from tkinter import *
import pymysql
from tkinter.messagebox import *




class addTeacher(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
        
    def db_teacher(self,name,position,telephone,subject,place,time):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
        name=name.get()
        position=position.get()
        telephone=telephone.get()
        place=place.get()
        subject=subject.get()
        time=time.get()
        print(name,position,telephone,subject,time)
        sql="insert into teacher (teacher_id,name,position,telephone,subject,place,time) values(uuid(),'%s','%s','%s','%s','%s','%s')"%(name,position,telephone,subject,place,time)
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
        Label(self,text="职称:").pack()
        position=Entry(self)
        position.pack()
        Label(self,text="电话:").pack()
        telephone=Entry(self)
        telephone.pack()
        Label(self,text="科目:").pack()
        subject=Entry(self)
        subject.pack()
        Label(self,text='教学地点').pack()
        place=Entry(self)
        place.pack()
        Label(self,text="教学时间:").pack()
        time=Entry(self)
        time.pack()
        button=Button(self,text="添加", command=lambda:self.db_teacher(name,position,telephone,subject,place,time))
        button.pack()


class addClass(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_class(self,class_id,num):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
        class_id=class_id.get()
        num=num.get()
        sql="insert into class (class_id,student_num,flag) values('%s','%s',0)"%(class_id,num)
        flag=cursor.execute(sql)
        conn.commit()
        if(flag==1):
                showinfo(message="添加数据成功")
        else:
                showinfo(message="添加数据失败")        
        cursor.close()
        conn.close()


    def createPage(self):
         Label(self,text="教室号:").pack()
         class_id=Entry(self)
         class_id.pack()
         Label(self,text="容纳人数").pack()
         num=Entry(self)
         num.pack()
         button=Button(self,text="增加",command=lambda:self.db_class(class_id,num))
         button.pack()


class deleteTeacher(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_deleteTeacher(self,name):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
        name=name.get()
        sql="delete from teacher where name='%s'"%(name)
        flag=cursor.execute(sql)
        conn.commit()
        if(flag==1):
                showinfo(message="删除数据成功")
        else:
                showinfo(message="删除数据失败")
        cursor.close()
        conn.close()
        
    def createPage(self):
        Label(self,text="名字：").pack()
        name=Entry(self)
        name.pack()
        Button(self,text="删除",command=lambda:self.db_deleteTeacher(name)).pack()



class deleteClass(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_deleteClass(self,class_id):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
        class_id=class_id.get()
        sql="delete from class where class_id='%s'"%(class_id)
        flag=cursor.execute(sql)
        conn.commit()
        if(flag==1):
                showinfo(message="删除数据成功")
        else:
                showinfo(message="删除数据失败")
        cursor.close()
        conn.close()

    def createPage(self):
        Label(self,text="教室名字").pack()
        class_id=Entry(self)
        class_id.pack()
        Button(self,text="删除",command=lambda:self.db_deleteClass(class_id)).pack()

class queryTeacher(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def db_queryTeacher(self,teacher_name):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
        teacher_name=teacher_name.get()
        sql="select name,telephone,subject,position,time,place from teacher where  name='%s'"%(teacher_name)
        row_account=cursor.execute(sql)
        rows=cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if(row_account==0):
                showinfo(message="数据库中没有此数据")
        else:
                var=StringVar()
                label=Label(self,textvariable=var)
                label.pack()
                str="名字:  "+rows[0][0]+"  职称:  "+rows[0][3]+"  联系方式:   "+rows[0][1]+"    教学科目: "+rows[0][2]+"    教学时间: "+rows[0][4] +" 教室："+rows[0][5]
                var.set(str)
    def createPage(self):
        Label(self,text="名字").pack()
        teacher_name=Entry(self)
        teacher_name.pack()
        Button(self,text="查询",command=lambda:self.db_queryTeacher(teacher_name)).pack()
               
class queryClass(Frame):
    def __init__(self,master=None):
         Frame.__init__(self,master)
         self.root=master
         self.createPage()
    def db_queryClass(self):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
       # query_id=query_id.get()
        sql="select class_id,student_num from class where flag=0"
        row_account=cursor.execute(sql)
        rows=cursor.fetchall()
        #print(row_account,rows)
        conn.commit()
        cursor.close()
        conn.close()
        if(row_account==0):
                showinfo(message="数据库中没有此数据")
        else:
            Label(self,text="空闲教室：").pack()
            for j in range(row_account):
                if j>=10:
                    break;
                var=StringVar()
                label=Label(self,textvariable=var)
                label.pack()
                str="教室号：  "+rows[j][0]+"    容纳人数:  "+rows[j][1]
                var.set(str)
    def db_queryClass_free(self):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
        cursor=conn.cursor()
       # query_id=query_id.get()
        sql="select class_id from class where flag=1"
        row_account=cursor.execute(sql)
        rows=cursor.fetchall()
        #print(row_account,rows)
        conn.commit()
        cursor.close()
        conn.close()
        if(row_account==0):
                showinfo(message="数据库中没有此数据")
        else:
                Label(self,text="教室使用情况").pack()
                for i in range(row_account):
                    sql="select name,telephone,subject,place,time from teacher where place='%s'"%(rows[i][0])
                    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='861153',db='db_project',charset='utf8')
                    cursor=conn.cursor()
                    j=cursor.execute(sql)
                    result=cursor.fetchall()
                    conn.commit()
                    cursor.close()
                    conn.close()
                    var=StringVar()
                    for er in range(j):
                        #print("e",result[j][0])
                        Label(self,textvariable=var).pack()
                        str="姓名： "+result[0][0]+"   联系方式   :"+result[0][1]+"   教学科目：  "+result[0][2]+"   教室:  "+result[0][3]+"   时间：  "+result[0][4]
                        var.set(str)
    def createPage(self):
        Label(self,text="查询空闲教室:").pack()
        Button(self,text="查询",command=self.db_queryClass).pack()
        Label(self,text='查询教室使用情况').pack()
        Button(self,text="查询",command=self.db_queryClass_free).pack()
        
        
class yourself_this(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def createPage(self):
        Label(self,text="小组成员：").pack()
        Label(self,text="杜珂   孙瑜琴  王晨  董亮亮  李榕").pack()

class system_this(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root=master
        self.createPage()
    def createPage(self):
        #imag=PhotoImage(file='D:\\logo.gif')
        #label=Label(self,image=imag).grid()
        Label(self,text="此系统为陕西理工大学李榕小组制作").grid()


