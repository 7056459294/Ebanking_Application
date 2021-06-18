#BLL
import tkinter as tk
import pushbullet 
import random as r
from tkinter import messagebox as mb
import Adafruit_IO as AD
import pymysql

global id1,paas1,mobno

i=AD.Client("mohitgahlot","aio_nwdN28ozEezU3TW0D1TjEk7Jkm4V")
pas1=i.receive("pwd").value
paas1=str(pas1)
id1="mohit123"
mobno="7056459294"


conn=pymysql.connect("127.0.0.1","root","","ebank")
cur=conn.cursor()
global btnlogin
def btnlogin():
    p=paas.get()
    i=id.get()
    if i==id1:
        if p==paas1:
           login.destroy()
           
           def exitcs():
               open.destroy()
               
           def newac():
               def dsub():
                   global otp4
                   m=mob.get()
                   otp4=r.randint(1000,9999)
                   pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
                   device=pb.devices[0]
                   pb.push_sms(device,f"{m}",f"YOUR OTP IS:\n{otp4}")
                   
                   
                   
               def fsub():
                   o=otp.get()
                   if str(otp4)==o:
                      try:
                         q="create table info1(Name varchar(50),Age int,Mob bigint(10),Bal bigint(20),Adress varchar(60),Acc varchar(20))"

                         cur.execute(q)
                         conn.commit()
                      except:
                             pass
                      Name=name.get()
                      Age=int(age.get())
                      Mob=int(mob.get())
                      Bal=int(bal.get())
                      Adress=add.get()
                      Acc=add.get()
                     
                      Acc=Name[0:2]+str(r.randint(100000,999999))+str(Age)
                      lbl11=tk.Label(newa,text=Acc,font=30,bg="yellow",fg="red",padx=5,pady=5)
                      lbl11.grid(row=9,column=1)
                      
                      q=f"insert into info1 values('{Name}',{Age},{Mob},{Bal},'{Adress}','{Acc}')"
                      cur.execute(q)
                      conn.commit()
                      
                      pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
                      device=pb.devices[0]
                      pb.push_sms(device,f"{Mob}",f"YOUR Account no:\n{Acc}")
                      mb.showinfo("LOGIN","Account created sucessfully")
                   else:
                        mb.showinfo("LOGIN","Enter Correct OTP")
                        otp.set("")
               def backf():
                   newa.destroy()
                   w1()
               open.destroy()
               
               newa=tk.Tk()
               newa.title("NEW ACCOUNT")
               newa.geometry("")
               newa.config(bg="sky blue",bd=5)
              
               lbl1=tk.Label(newa,text="Name:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl1.grid(row=1,column=0)
               lbl2=tk.Label(newa,text="Age:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl2.grid(row=2,column=0)
               lbl4=tk.Label(newa,text="Mobile no.:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl4.grid(row=3,column=0)
               lbl5=tk.Label(newa,text="Adress:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl5.grid(row=4,column=0)
               lbl6=tk.Label(newa,text="Balance:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl6.grid(row=5,column=0)
               lbl7=tk.Label(newa,text="OTP:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl7.grid(row=7,column=0)
               lbl8=tk.Label(newa,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl8.grid(row=9,column=0)
               
               name=tk.StringVar()
               entr=tk.Entry(newa,textvariable=name)
               entr.grid(row=1,column=1)
               age=tk.StringVar()
               entr=tk.Entry(newa,textvariable=age)
               entr.grid(row=2,column=1)
               mob=tk.StringVar()
               entr=tk.Entry(newa,textvariable=mob)
               entr.grid(row=3,column=1)
               add=tk.StringVar()
               entr=tk.Entry(newa,textvariable=add)
               entr.grid(row=4,column=1)
               bal=tk.StringVar()
               entr=tk.Entry(newa,textvariable=bal)
               entr.grid(row=5,column=1)
               otp=tk.StringVar()
               entr=tk.Entry(newa,textvariable=otp)
               entr.grid(row=7,column=1)
               
               btn1=tk.Button(newa,text="SUBMIT",font=20,command=dsub)
               btn1.grid(row=6,column=1)
               btn2=tk.Button(newa,text="SUBMIT",font=20,command=fsub)
               btn2.grid(row=8,column=1)
               btn3=tk.Button(newa,text="Back",font=20,command=backf)
               btn3.grid(row=10,column=1)
               
           def mgac():
               open.destroy()
               
               def ext():
                   mgac.destroy()
                   w1()
                   
               def acsub():
                   global acc
                   acc=ac.get()
                   def dsub():
                       n=name.get()
                       a=int(age.get())
                       m=int(mob.get())
                       ad=add.get()
                       
                       q=f"update info1 set Name='{n}',Age={a},Mob={m},Adress='{ad}' where Acc='{acc}'"
                       cur.execute(q)
                       conn.commit()
                       mb.showinfo("LOGIN","Account modify sucessfully")
                   lbl1=tk.Label(mgac,text="Name:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl1.grid(row=2,column=0)
                   lbl2=tk.Label(mgac,text="Age:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl2.grid(row=3,column=0)
                   lbl4=tk.Label(mgac,text="Mobile no.:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl4.grid(row=4,column=0)
                   lbl5=tk.Label(mgac,text="Adress:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl5.grid(row=5,column=0)
                   
                   name=tk.StringVar()
                   entr=tk.Entry(mgac,textvariable=name)
                   entr.grid(row=2,column=1)
                   age=tk.StringVar()
                   entr=tk.Entry(mgac,textvariable=age)
                   entr.grid(row=3,column=1)
                   mob=tk.StringVar()
                   entr=tk.Entry(mgac,textvariable=mob)
                   entr.grid(row=4,column=1)
                   add=tk.StringVar()
                   entr=tk.Entry(mgac,textvariable=add)
                   entr.grid(row=5,column=1)
                   
                   btn1=tk.Button(mgac,text="SUBMIT",font=20,command=dsub)
                   btn1.grid(row=6,column=1)
                   
               mgac=tk.Tk()
               mgac.title("MANAGE ACCOUNTS")
               mgac.geometry("")
               mgac.config(bg="sky blue",bd=5)
               lbl1=tk.Label(mgac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl1.grid(row=0,column=0)
               ac=tk.StringVar()
               entr1=tk.Entry(mgac,textvariable=ac)
               entr1.grid(row=0,column=1)
               btn1=tk.Button(mgac,text="SUBMIT",font=20,command=acsub)
               btn1.grid(row=1,column=1)
               btn3=tk.Button(mgac,text="Exit",font=20,command=ext)
               btn3.grid(row=1,column=0)
               
               pass
           def srac():
               def acsub():
                   acc=ac.get()
                  
                   lbl1=tk.Label(srac,text="Name:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl1.grid(row=4,column=0)
                   lbl2=tk.Label(srac,text="Age:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl2.grid(row=5,column=0)
                   lbl4=tk.Label(srac,text="Mobile no.:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl4.grid(row=6,column=0)
                   lbl5=tk.Label(srac,text="Balance:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl5.grid(row=7,column=0)
                   lbl6=tk.Label(srac,text="Adress:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl6.grid(row=8,column=0)
                   lbl8=tk.Label(srac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl8.grid(row=9,column=0)
                   
                   q=f"select * from info1 where Acc='{acc}'"
                   cur.execute(q)
                   conn.commit()
                   for name,age,mob,bal,add,acc in cur:
                        name,age,mob,bal,add,acc
                   
                   lbl9=tk.Label(srac,text=name,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl9.grid(row=4,column=1)
                   lbl10=tk.Label(srac,text=age,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl10.grid(row=5,column=1)
                   lbl11=tk.Label(srac,text=mob,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl11.grid(row=6,column=1)
                   lbl12=tk.Label(srac,text=bal,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl12.grid(row=7,column=1)
                   lbl13=tk.Label(srac,text=add,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl13.grid(row=8,column=1)
                   lbl15=tk.Label(srac,text=acc,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl15.grid(row=9,column=1)
                   acc.set("")
                   
               def msub():
                   m=mb.get()
                  
                   lbl1=tk.Label(srac,text="Name:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl1.grid(row=4,column=0)
                   lbl2=tk.Label(srac,text="Age:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl2.grid(row=5,column=0)
                   lbl4=tk.Label(srac,text="Mobile no.:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl4.grid(row=6,column=0)
                   lbl5=tk.Label(srac,text="Balance:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl5.grid(row=7,column=0)
                   lbl6=tk.Label(srac,text="Adress:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl6.grid(row=8,column=0)
                   lbl8=tk.Label(srac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl8.grid(row=9,column=0)
                   
                   q=f"select * from info1 where Mob={m}"
                   cur.execute(q)
                   conn.commit()
                   for name,age,mob,bal,add,acc in cur:
                        name,age,mob,bal,add,acc
                   
                   lbl9=tk.Label(srac,text=name,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl9.grid(row=4,column=1)
                   lbl10=tk.Label(srac,text=age,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl10.grid(row=5,column=1)
                   lbl11=tk.Label(srac,text=mob,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl11.grid(row=6,column=1)
                   lbl12=tk.Label(srac,text=bal,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl12.grid(row=7,column=1)
                   lbl13=tk.Label(srac,text=add,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl13.grid(row=8,column=1)
                   lbl15=tk.Label(srac,text=acc,font=30,bg="yellow",fg="blue",padx=5,pady=5)
                   lbl15.grid(row=9,column=1)
                   mb.set("")
               def ext():
                   srac.destroy()
                   w1()
               
               
               open.destroy()
               
               srac=tk.Tk()
               srac.title("SEARCH ACCOUNTS")
               srac.geometry("")
               srac.config(bg="sky blue",bd=5)
               
               lbl1=tk.Label(srac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl1.grid(row=0,column=0)
               ac=tk.StringVar()
               entr1=tk.Entry(srac,textvariable=ac)
               entr1.grid(row=0,column=1)
               btn1=tk.Button(srac,text="SUBMIT",font=20,command=acsub)
               btn1.grid(row=1,column=1)
               lbl2=tk.Label(srac,text="Mobile no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl2.grid(row=2,column=0)
               mb=tk.StringVar()
               entr2=tk.Entry(srac,textvariable=mb)
               entr2.grid(row=2,column=1)
               btn2=tk.Button(srac,text="SUBMIT",font=20,command=msub)
               btn2.grid(row=3,column=1)
               btn3=tk.Button(srac,text="Exit",font=20,command=ext)
               btn3.grid(row=3,column=0)
               
           def dlac():
               open.destroy()
               
               def acsub():
                   acc=ac.get()
                  
                   
                   q=f"delete from info1 where Acc='{acc}'"
                   cur.execute(q)
                   conn.commit()
                   
                   mb.showinfo("LOGIN","Account delete sucessfully")
                   acc.set("")
                  
                   
               def msub():
                   m=mb1.get()
                  
                   
                   q=f"delete from info1 where Mob={m}"
                   cur.execute(q)
                   conn.commit()
                   
                   mb.showinfo("LOGIN","Account delete sucessfully")
                   mb1.set("")
               def ext():
                   dlac.destroy()
                   w1()              
               
               dlac=tk.Tk()
               dlac.title("dELETE ACCOUNTS")
               dlac.geometry("")
               dlac.config(bg="sky blue",bd=5)
               
               lbl1=tk.Label(dlac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl1.grid(row=0,column=0)
               ac=tk.StringVar()
               entr1=tk.Entry(dlac,textvariable=ac)
               entr1.grid(row=0,column=1)
               btn1=tk.Button(dlac,text="SUBMIT",font=20,command=acsub)
               btn1.grid(row=1,column=1)
               lbl2=tk.Label(dlac,text="Mobile no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
               lbl2.grid(row=2,column=0)
               mb1=tk.StringVar()
               entr2=tk.Entry(dlac,textvariable=mb1)
               entr2.grid(row=2,column=1)
               btn2=tk.Button(dlac,text="SUBMIT",font=20,command=msub)
               btn2.grid(row=3,column=1)
               btn3=tk.Button(dlac,text="Exit",font=20,command=ext)
               btn3.grid(row=3,column=0)
           def balac():
                def wdlac():
                   def subd():
                       
                       bale=bal.get()
                       bale=int(bale)
                      
                       ace=ac.get()
                       
                       
                       q=f"select * from info1 where Acc='{ace}'"
                       cur.execute(q)
                       conn.commit()
                       for name,age,mob,bali,add,acc in cur:
                           name,age,mob,bali,add,acc
                       
                    
                       if bali>=bale:
                            bals=bali-bale
                            q=f"update info1 set Bal={bals} where Acc='{ace}'"
                            cur.execute(q)
                            conn.commit()
                            lbl1=tk.Label(wdac,text="Total Ammount:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                            lbl1.grid(row=5,column=0)
                            lbl2=tk.Label(wdac,text=bals,font=30,bg="yellow",fg="red",padx=5,pady=5)
                            lbl2.grid(row=5,column=1)
                            pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
                            device=pb.devices[0]
                            pb.push_sms(device,f"{mob}",f"ACCOUNT:{acc} \n WITHDRAWAL : Rs.{bale}\n TOTAL BALANCE : RS.{bals} ")
                        
                            mb.showinfo("LOGIN","Ammount withdrawal sucessfully")
                            
                       else:
                           mb.showinfo("LOGIN",f"srry try again your balance is:{bali}")
                   def extd():
                       wdac.destroy()
                       w1()
                   lbl1=tk.Label(wdac,text="Ammount:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                   lbl1.grid(row=2,column=0)
                   bal=tk.StringVar()
                   entr1=tk.Entry(wdac,textvariable=bal)
                   entr1.grid(row=2,column=1)
                   btn3=tk.Button(wdac,text="SUBMIT",font=20,command=subd)
                   btn3.grid(row=3,column=1)
                   btn3=tk.Button(wdac,text="Exit",font=20,command=extd)
                   btn3.grid(row=4,column=1)
                def dpac():
                    def subd():
                        
                       bale=bal.get()
                       bale=int(bale)
                      
                       ace=ac.get()
                       
                       
                       q=f"select * from info1 where Acc='{ace}'"
                       cur.execute(q)
                       conn.commit()
                       for name,age,mob,bali,add,acc in cur:
                          name,age,mob,bali,add,acc
                       
                    
                 
                       bals=bali+bale
                       q=f"update info1 set Bal={bals} where Acc='{ace}'"
                       cur.execute(q)
                       conn.commit()
                       lbl1=tk.Label(wdac,text="Total Ammount:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                       lbl1.grid(row=5,column=0)
                       lbl2=tk.Label(wdac,text=bals,font=30,bg="yellow",fg="red",padx=5,pady=5)
                       lbl2.grid(row=5,column=1)
                       pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
                       device=pb.devices[0]
                       pb.push_sms(device,f"{mob}",f"ACCOUNT:{acc} \n Deposit : Rs.{bale}\n TOTAL BALANCE: RS.{bals} ")
                        
                       mb.showinfo("LOGIN","Ammount Deposit sucessfully")
                            
                      
                    def extd():
                       wdac.destroy()
                       w1()
                    lbl1=tk.Label(wdac,text="Ammount:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                    lbl1.grid(row=2,column=0)
                    bal=tk.StringVar()
                    entr1=tk.Entry(wdac,textvariable=bal)
                    entr1.grid(row=2,column=1)
                    btn3=tk.Button(wdac,text="SUBMIT",font=20,command=subd)
                    btn3.grid(row=3,column=1)
                    btn3=tk.Button(wdac,text="Exit",font=20,command=extd)
                    btn3.grid(row=4,column=1)
                open.destroy()
                wdac=tk.Tk()
                wdac.title("W & D")
                wdac.geometry("")
                wdac.config(bg="sky blue",bd=5)
                lbl1=tk.Label(wdac,text="Account no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
                lbl1.grid(row=0,column=0)
                global ac
                ac=tk.StringVar()
                entr1=tk.Entry(wdac,textvariable=ac)
                entr1.grid(row=0,column=1)
                btn1=tk.Button(wdac,text="WITHDRAWAL",font=20,command=wdlac)
                btn1.grid(row=1,column=0)
                btn2=tk.Button(wdac,text="DEPOSIT",font=20,command=dpac)
                btn2.grid(row=1,column=1)
           
                 
                      
               
              
              
           def btnxt():
               open.destroy()
               w1()
        
           
           open=tk.Tk()
           open.title("BANK")
           open.geometry("500x500")
           open.config(bg="sky blue",bd=5)
           wlcmlbl=tk.Label(open,text=f"!!!! Welcome !!!! \n{id1}",font=50,bg="sky blue",fg="red",padx=5,pady=5)
           wlcmlbl.pack()
           btnnew=tk.Button(open,text="New Account",font=30,padx=10,pady=10,bg="yellow",fg="red",bd=5,command=newac)
           btnnew.pack()
           btnsr=tk.Button(open,text="Search Accounts",font=30,padx=10,pady=10,bg="yellow",fg="red",bd=5,command=srac)
           btnsr.pack()
           btndl=tk.Button(open,text="Delete Accounts",font=30,padx=10,pady=10,bg="yellow",fg="red",bd=5,command=dlac)
           btndl.pack()
           btnmd=tk.Button(open,text="Manage Accounts",font=30,padx=10,pady=10,bg="yellow",fg="red",bd=5,command=mgac)
           btnmd.pack()
           btnbm=tk.Button(open,text="Withdral & Deposit",font=30,padx=10,pady=10,bg="yellow",fg="red",bd=5,command=balac)
           btnbm.pack()
           btnexit=tk.Button(open,text="Exit",font=30,padx=10,pady=10,bg="red",fg="yellow",bd=5,command=btnxt)
           btnexit.pack()
           
        else:
            mb.showinfo("LOGIN","Enter Correct pasword")
    else:
         mb.showinfo("LOGIN","Enter Correct id")
         
def btnexit():
    login.destroy()
    
  
    
def forgotpaas():
    login.destroy()
    def mobsub():
        global m
        m=mob.get()
        if m==mobno:
            global otp
            otp=r.randint(1000,9999)
            pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
            device=pb.devices[0]
            pb.push_sms(device,f"{m}",f"YOUR OTP IS:\n{otp}")
        else:
            mb.showinfo("LOGIN","Enter Correct Mobile Number")
            mob.set("")
    def otpsub():
        global o
        o=otp1.get()
        if o==str(otp):
             mb.showinfo("LOGIN","!!!!!OTP VERIFY!!!!")
        else:
             mb.showinfo("LOGIN","Enter Correct Otp")
             otp1.set("")
    def newsub():
        if m==mobno:
           if o==str(otp): 
              newp=newpass.get()
              i=AD.Client("mohitgahlot","aio_nwdN28ozEezU3TW0D1TjEk7Jkm4V")
              i.send("pwd",f"{newp}")
              mb.showinfo("LOGIN","!!!!Password change sucessfully!!!!")
              pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
              device=pb.devices[0]
              pb.push_sms(device,f"{m}",f"YOUR NEW PASSWORD IS:\n{newp}")

           else:
              mb.showinfo("LOGIN","Enter Correct Otp")
    def backlogin():
         mobv.destroy()
         w1()
              
    mobv=tk.Tk()
    mobv.title("LOGIN")
    mobv.geometry("")
    mobv.config(bg="sky blue")
        
        
    moblbl=tk.Label(mobv,text="Mobile no:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
    moblbl.grid(row=0,column=0)
    otplbl=tk.Label(mobv,text="Otp:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
    otplbl.grid(row=2,column=0)
    otpnewpass=tk.Label(mobv,text="New password:-:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
    otpnewpass.grid(row=4,column=0)
    
    btnsubm=tk.Button(mobv,text="SUBMIT",font=20,command=mobsub)
    btnsubm.grid(row=1,column=1)
    btnsubo=tk.Button(mobv,text="SUBMIT",font=20,command=otpsub)
    btnsubo.grid(row=3,column=1)
    btnsubm=tk.Button(mobv,text="SUBMIT",font=20,command=newsub)
    btnsubm.grid(row=5,column=1)
    btnbk=tk.Button(mobv,text="BACK",font=20,command=backlogin)
    btnbk.grid(row=5,column=0)
    
    global mob    
    mob=tk.StringVar()
    mobentr=tk.Entry(mobv,textvariable=mob)
    mobentr.grid(row=0,column=1)
    global otp1
    otp1=tk.StringVar()
    otpentr=tk.Entry(mobv,textvariable=otp1)
    otpentr.grid(row=2,column=1)     
    global newpass
    newpass=tk.StringVar()
    newpwd=tk.Entry(mobv,textvariable=newpass)
    newpwd.grid(row=4,column=1)
def w1():
    global login
    login=tk.Tk()
    login.title("LOGIN")
    login.geometry("")
    login.config(bg="sky blue")    
        
    
    id_lbl=tk.Label(login,text="ID:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
    id_lbl.grid(row=0,column=0)
    paas_lbl=tk.Label(login,text="PASSWORD:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
    paas_lbl.grid(row=1,column=0)
        
      
    btn_login=tk.Button(login,text="LOGIN",font=20,command=btnlogin)
    btn_login.grid(row=3,column=1)
    btn_forgotpaas=tk.Button(login,text="FORGOT PASSWORD",font=20,command=forgotpaas)
    btn_forgotpaas.grid(row=4,column=1)
    btn_exit=tk.Button(login,text="EXIT",font=20,command=btnexit)
    btn_exit.grid(row=3,column=0) 
        
    global id
    id=tk.StringVar()
    entr_id=tk.Entry(login,textvariable=id)
    entr_id.grid(row=0,column=1)
    global paas
    paas=tk.StringVar()
    entr_paas=tk.Entry(login,textvariable=paas,show="*")
    entr_paas.grid(row=1,column=1)

w1()
tk.mainloop()