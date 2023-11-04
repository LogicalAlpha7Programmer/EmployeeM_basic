from tkinter import *
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
#import pandas
import time
import re
import pickle
import os
#import sqlite3


def main(root):
    FileName = 'untitled'
    root.title(FileName)
    root.config(bg="light blue")
    root.geometry("1100x700+200+50")
    root.resizable(True, True)

    def tick():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clock.config(text='Date: ' + date_string + "\n" + "Time: " + time_string)
        clock.after(200, tick)

    def addemployee():
        def submitadd():

            PID = personalidval.get() #getting data from entries...or entry lables
            EID = employeeidval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            salary = salaryval.get()
            addedtime = time.strftime("%H:%M:%S") #to get time
            addeddate = time.strftime("%d/%m/%Y")
            city = cityval.get()
            curncy = curncyval.get()
            vv = [PID,EID,name,mobile,email,address,gender,salary,addeddate,addedtime,city]
            for p in phnPatterns:
              if re.search(p,mobile) and re.search(Emailregex,email) and vv not in datas[0] and curncy in curncyvals and " " not in vv[7][:] and re.search(idregex,vv[0]):

                      vv[7] = salary+" "+curncy.upper()
                      datas[0].append(vv)
                      cleartable()
                      for i in datas[0]:
                          employeetable.insert('',END,values = i)
                      personalidval.set('')
                      employeeidval.set('')
                      nameval.set('')
                      mobileval.set('')
                      emailval.set('')
                      addressval.set('')
                      genderval.set('')
                      salaryval.set('')
                      cityval.set('')
                      curncyval.set('')

        
        addroot = Toplevel(master=DataEntryFrame)
        addroot.grab_set()
        addroot.geometry('470x590+220+200')
        addroot.title('Enter details')
        addroot.config(bg='light blue')
        addroot.resizable(False, True) #making window nonresizable

        # ------------------------- Addemployee Labels
        
        personalidlabel = Label(addroot, text=' Personal Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
        personalidlabel.place(x=10, y=10)

        employeeidlabel = Label(addroot, text=' Customer Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        employeeidlabel.place(x = 10, y=10+60)

        namelabel = Label(addroot, text=' Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        namelabel.place(x=10, y=70+60)

        mobilelabel = Label(addroot, text=' Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        mobilelabel.place(x=10, y=130+60)

        emaillabel = Label(addroot, text=' Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        emaillabel.place(x=10, y=190+60)

        addresslabel = Label(addroot, text=' Address: ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                             borderwidth=3, width=12, anchor='w')
        addresslabel.place(x=10, y=250+60)  # DCAE96

        genderlabel = Label(addroot, text=' Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        genderlabel.place(x=10, y=310+60)

        curncylabel = Label(addroot, text=' Currency : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        curncylabel.place(x=10, y=370+60)

        salarylabel = Label(addroot, text=' Salary/Month : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        salarylabel.place(x=10, y=370+60+60)

        citylabel = Label(addroot, text=' City : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        citylabel.place(x=10, y=370+60+60+60)
        
        #------------------- Addemployee Entry
        personalidval = StringVar()
        employeeidval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        salaryval = StringVar()
        cityval = StringVar()
        curncyval = StringVar()

        #------------------- Addemployee entry lables
        personalidentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=personalidval, width=18)
        personalidentry.place(x=250, y=10)

        employeeidentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=employeeidval, width=18)
        employeeidentry.place(x=250, y=10+60)

        nameentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=nameval, width=18)
        nameentry.place(x=250, y=70+60)

        mobileentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=mobileval, width=18)
        mobileentry.place(x=250, y=130+60)

        emailentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=emailval, width=18)
        emailentry.place(x=250, y=190+60)

        addressentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=addressval, width=18)
        addressentry.place(x=250, y=250+60)

        genderentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=genderval, width=18)
        genderentry.place(x=250, y=310+60)

        curncyFr = Frame(addroot)
        curncyFr.pack()    
        curncyFr.place(x=250, y=370+60)

        comboCurncy = ttk.Combobox(curncyFr, values=curncyvals, width = 16, font=('Helvetica', 15, 'bold'), textvariable=curncyval)
        comboCurncy.pack(side = 'left',expand = True)

        salaryentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=salaryval, width=18)
        salaryentry.place(x=250,y=370+60+60)

        
        cityentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=cityval, width=18)
        cityentry.place(x=250, y=420+60+60+10)
        #------------------------- addemployee submit button
        submitbtn = Button(addroot, text="Submit", bd=3, font=("Bodoni", 16, "bold"), width=10)
        submitbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue", command=submitadd)
        submitbtn.place(x=150, y=420+60+60+60)

        addroot.mainloop()

        

    def commandemployee():

        def updateE():

            PID = personalidval.get()
            EID = employeeidval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            salary = salaryval.get()
            addeddate = dateval.get()
            addedtime = timeval.get()
            city = cityval.get()

            def update():

                newPID = newpersonalidval.get()
                newEID = newemployeeidval.get()
                newname = newnameval.get()
                newmobile = newmobileval.get()
                newemail = newemailval.get()
                newaddress = newaddressval.get()
                newgender = newgenderval.get()
                newsalary = newsalaryval.get()
                newdate = newdateval.get()
                newtime = newtimeval.get()
                newcity = newcityval.get()
                if newdate != addeddate and newtime != addedtime:
                  newdate.set(addeddate)
                  newtime.set(addedtime)
                oldvv = [PID,EID,name,mobile,email,address,gender,salary,addeddate,addedtime,city]
                newvv = [newPID,newEID,newname,newmobile,newemail,newaddress,newgender,newsalary,newdate,newtime,newcity]
                for P in phnPatterns:
                  if re.search(P,newmobile) and re.search(Emailregex,newemail) and newvv not in datas[0] and re.search(idregex,newvv[0]):
                      messagebox.showinfo('Notifications', 'Emplayee Id {} is Edited Succesfully....'.format(EID), parent=updateroot)
                      if oldvv in datas[0] and newvv not in datas[0] or newvv in datas[0]:
                        datas[0].remove(oldvv)
                        datas[0].append(newvv)
                        cleartable()    
                        for i in datas[0]:
                              vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                              employeetable.insert('',END,values=vv)
                        updateroot.destroy()
                  elif oldvv not in datas[0]:
                      messagebox.showerror('ERROR','Your inputs is not in the Table!')
            vv3 = [PID,EID,name,mobile,email,address,gender,salary,addeddate,addedtime,city]
            for p in phnPatterns:
              if re.search(p,mobile) and re.search(Emailregex,email) and vv3 in datas[0] and re.search(idregex,vv3[0]):
                

                updateroot = Toplevel(master=DataEntryFrame)
                updateroot.grab_set()
                updateroot.geometry('990x585+220+160')
                updateroot.title('Update Record')
                updateroot.config(bg='light blue')
                updateroot.resizable(True, True)


                newpersonalidlabel = Label(updateroot, text=' Personal Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                borderwidth=3, width=12, anchor='w')
                newpersonalidlabel.place(x=10, y=10)

                newemployeeidlabel = Label(updateroot, text=' Employee Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                borderwidth=3, width=12, anchor='w')
                newemployeeidlabel.place(x=10,y=10+60)

                newnamelabel = Label(updateroot, text=' Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                  borderwidth=3, width=12, anchor='w')
                newnamelabel.place(x=10, y=70+60)

                newmobilelabel = Label(updateroot, text=' Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                    borderwidth=3, width=12, anchor='w')
                newmobilelabel.place(x=10, y=130+60)

                newemaillabel = Label(updateroot, text=' Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                   borderwidth=3, width=12, anchor='w')
                newemaillabel.place(x=10, y=190+60)

                newaddresslabel = Label(updateroot, text=' Address: ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                     borderwidth=3, width=12, anchor='w')
                newaddresslabel.place(x=10, y=250+60)  # DCAE96

                newgenderlabel = Label(updateroot, text=' Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                    borderwidth=3, width=12, anchor='w')
                newgenderlabel.place(x=10, y=310+60)

                newsalarylabel = Label(updateroot, text=' Salary/Month : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                    borderwidth=3, width=12, anchor='w')
                newsalarylabel.place(x=10, y=370+60)

                newdatelabel = Label(updateroot, text=' Added Date : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                  borderwidth=3, width=12, anchor='w')
                newdatelabel.place(x=490, y=10)

                newtimelabel = Label(updateroot, text=' Added Time : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                  borderwidth=3, width=12, anchor='w')
                newtimelabel.place(x=490, y=70)

                newcitylabel = Label(updateroot, text=' City : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                                  borderwidth=3, width=12, anchor='w')
                newcitylabel.place(x=490, y=70+60)


                newpersonalidval = StringVar()
                newemployeeidval = StringVar()
                newnameval = StringVar()
                newmobileval = StringVar()
                newemailval = StringVar()
                newaddressval = StringVar()
                newgenderval = StringVar()
                newsalaryval = StringVar()
                newdateval = StringVar()
                newtimeval = StringVar()
                newcityval = StringVar()

                newpersonalidval.set(personalidval.get())
                newemployeeidval.set(employeeidval.get())
                newnameval.set(nameval.get())
                newmobileval.set(mobileval.get())
                newemailval.set(emailval.get())
                newaddressval.set(addressval.get())
                newgenderval.set(genderval.get())
                newsalaryval.set(salaryval.get())
                newdateval.set(dateval.get())
                newtimeval.set(timeval.get())
                newcityval.set(cityval.get())
                

                newpersonalidentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newpersonalidval)
                newpersonalidentry.place(x=250, y=10)

                newemployeeidentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newemployeeidval)
                newemployeeidentry.place(x=250, y=10+60)


                newnameentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newnameval)
                newnameentry.place(x=250, y=70+60)

                newmobileentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newmobileval)
                newmobileentry.place(x=250, y=130+60)

                newemailentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newemailval)
                newemailentry.place(x=250, y=190+60)

                newaddressentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newaddressval)
                newaddressentry.place(x=250, y=250+60)

                newgenderentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newgenderval)
                newgenderentry.place(x=250, y=310+60)

                newsalaryentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newsalaryval)
                newsalaryentry.place(x=250, y=370+60)


                newdateentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newdateval)
                newdateentry.place(x=720, y=10)

                newtimeentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newtimeval)
                newtimeentry.place(x=720, y=10+60)

                newcityentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=newcityval)
                newcityentry.place(x=720, y=70+60)

                newtimeentry.config(state = 'disabled')
                newdateentry.config(state = 'disabled')

                updatebtn = Button(updateroot, text="Apply", bd=3, font=("Bodoni", 16, "bold"), width=10,command=update)
                updatebtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue")
                updatebtn.place(x=720, y=70+60+60)


                updateroot.mainloop()

        def restoreE():
            PID = personalidval.get()
            EID = employeeidval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            salary = salaryval.get()
            date = dateval.get()
            time = timeval.get()
            city = cityval.get()
            vv = [PID,EID,name,mobile,email,address,gender,salary,date,time,city]
            if vv not in datas[0] and vv in quitEli or vv in fireEli:
                if vv in quitEli:
                    quitEli.remove(vv)
                elif vv in fireEli:
                    fireEli.remove(vv)
                datas[0].append(vv)
                showemployees(searchtarget[-1])                

        def deleteE():
            PID = personalidval.get()
            EID = employeeidval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            salary = salaryval.get()
            date = dateval.get()
            time = timeval.get()
            city = cityval.get()
            vv4 = [PID,EID,name,mobile,email,address,gender,salary,date,time,city]
            def quitted():
                PID = personalidval.get()
                EID = employeeidval.get()
                name = nameval.get()
                mobile = mobileval.get()
                email = emailval.get()
                address = addressval.get()
                gender = genderval.get()
                salary = salaryval.get()
                date = dateval.get()
                time = timeval.get()
                city = cityval.get()
                reason = t.get(1.0,END)
                vv = [PID,EID,name,mobile,email,address,gender,salary,date,time,city,reason]
                
                for p in phnPatterns:
                  if re.search(p,mobile) and re.search(Emailregex,email) and vv[:11] in datas[0]:
                    if vv[:11] in datas[0]:
                      quitEli.append(vv)
                      datas[0].remove(vv[:11])

                      showpressedemployees(datas[0],fireElibtnstate='normal',quitElibtnstate='normal',curntElibtnstate='disabled')

                      CR.destroy()
                    else:
                      messagebox.showerror('ERROR','Your inputs is not in the tabel')

            def fired():
                PID = personalidval.get()
                EID = employeeidval.get()
                name = nameval.get()
                mobile = mobileval.get()
                email = emailval.get()
                address = addressval.get()
                gender = genderval.get()
                salary = salaryval.get()
                date = dateval.get()
                time = timeval.get()
                city = cityval.get()
                reason = t.get(1.0,END)
                vv = [PID,EID,name,mobile,email,address,gender,salary,date,time,city,reason]
                
                for p in phnPatterns:
                  if re.search(p,mobile) and re.search(Emailregex,email) and vv[:11] in datas[0]:
                    if vv[:11] in datas[0]:
                      fireEli.append(vv)
                      datas[0].remove(vv[:11])

                      showpressedemployees(datas[0],fireElibtnstate='normal',quitElibtnstate='normal',curntElibtnstate='disabled')


                      CR.destroy()
                    else:
                      messagebox.showerror('ERROR','Your inputs is not in the tabel')
            for p in phnPatterns:
                if(re.search(p,mobile) and re.search(Emailregex,email) and vv4 in datas[0]):
                    dr = Toplevel(master=CR)
                    dr.grab_set()
                    dr.geometry('590x215+220+160')
                    dr.title('Delete')
                    dr.config(bg='light blue')
                    dr.resizable(False, False)       
                    tFrame = Frame(dr, bg='Lavender', relief=GROOVE, borderwidth=5)

                    scroll_x = Scrollbar(tFrame, orient=HORIZONTAL)
                    scroll_y = Scrollbar(tFrame, orient=VERTICAL)


                    btnframebottomc = Frame(dr)
                    btnframebottomc.pack(side='bottom')
                    Button(btnframebottomc, text="Quit Emplyee", bd=3, font=("Bodoni", 16, "bold"), command = quitted, width=15).pack(side='left')
                    Button(btnframebottomc, text="Fire Emplyee", bd=3, font=("Bodoni", 16, "bold"), command = fired, width=15).pack(side='left')

                    tFrame.pack(side='bottom')

                    t = Text(tFrame, height = 10, width = 52)
                    t.pack()

                    scroll_x.config(command = t.xview)
                    scroll_y.config(command = t.yview)
                    t.insert(END,'Reason Why?...')
                    
                    dr.mainloop()

        CR = Toplevel(master=DataEntryFrame)
        CR.grab_set()
        CR.geometry('990x585+220+160')
        CR.title('Update Record')
        CR.config(bg='light blue')
        CR.resizable(True, True)

        personalidlabel = Label(CR, text=' Personal Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
        personalidlabel.place(x=10, y=10)

        employeeidlabel = Label(CR, text=' Employee Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
        employeeidlabel.place(x=10,y=10+60)
        
        namelabel = Label(CR, text=' Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        namelabel.place(x=10, y=70+60)

        mobilelabel = Label(CR, text=' Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        mobilelabel.place(x=10, y=130+60)

        emaillabel = Label(CR, text=' Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        emaillabel.place(x=10, y=190+60)

        addresslabel = Label(CR, text=' Address : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                             borderwidth=3, width=12, anchor='w')
        addresslabel.place(x=10, y=250+60)  # DCAE96

        genderlabel = Label(CR, text=' Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        genderlabel.place(x=10, y=310+60)

        salarylabel = Label(CR, text=' Salary/Month : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
        salarylabel.place(x=10, y=370+60)

        datelabel = Label(CR, text=' Added Date : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        datelabel.place(x=490, y=10)

        timelabel = Label(CR, text=' Added Time : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        timelabel.place(x=490, y=70)

        citylabel = Label(CR, text=' City : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        citylabel.place(x=490, y=70+60)


        personalidval = StringVar()
        employeeidval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        salaryval = StringVar()
        dateval = StringVar()
        timeval = StringVar()
        cityval = StringVar()


        personalidentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=personalidval)
        personalidentry.place(x=250, y=10)

        employeeidentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=employeeidval)
        employeeidentry.place(x=250, y=10+60)


        nameentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=nameval)
        nameentry.place(x=250, y=70+60)

        mobileentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=mobileval)
        mobileentry.place(x=250, y=130+60)

        emailentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=emailval)
        emailentry.place(x=250, y=190+60)

        addressentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=addressval)
        addressentry.place(x=250, y=250+60)

        genderentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=genderval)
        genderentry.place(x=250, y=310+60)

        salaryentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=salaryval)
        salaryentry.place(x=250, y=370+60)

        dateentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=dateval)
        dateentry.place(x=720, y=10)

        timeentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=timeval)
        timeentry.place(x=720, y=70)
        
        cityentry = Entry(CR, font=('arial', 12, 'bold'), bd=5, textvariable=cityval)
        cityentry.place(x=720, y=70+60)

        btnframe=Frame(CR)
        btnframe.pack()
        btnframe.place(x=490,y=70+60+60)
        delbtn = Button(btnframe, text="Delete Employee", bd=3, font=("Bodoni", 16, "bold"), width=15)
        delbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue", command=deleteE)
        delbtn.pack(side=BOTTOM,expand=True)
        updbtn = Button(btnframe, text="Edit Empolyee", bd=3, font=("Bodoni", 16, "bold"), width=15)
        updbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue", command=updateE)
        updbtn.pack(side=BOTTOM,expand=True)
        restrbtn = Button(btnframe, text="Restore Empolyee", bd=3, font=("Bodoni", 16, "bold"), width=15)
        restrbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue", command=restoreE)        
        restrbtn.pack(side = 'bottom',expand = True)



        if (len(searchtarget[-1]) == len(datas[0])):
            restrbtn.config(state = 'disabled')
            delbtn.config(state = 'normal')
        if (len(searchtarget[-1]) == len(quitEli)):
            delbtn.config(state = 'disabled')
            restrbtn.config(state = 'normal')

        cc = employeetable.focus()      #this will get all details of existing record when clicked on it and fills in update entryform
        content = employeetable.item(cc)
        pp = content['values']
        if (len(pp) != 0):
            for i in searchtarget[-1]:
                if pp[2] == i[2] and pp[4] == i[4] and pp[5] == i[5] and pp[6] == i[6] and pp[7] == i[7] and pp[8] == i[8] and pp[9] == i[9] and pp[10] == i[10]:
                    vv = [i[0], i[1], pp[2], i[3], pp[4], pp[5], pp[6], pp[7], pp[8], pp[9], pp[10]]
                    if vv in searchtarget[-1]:
                        personalidval.set(i[0])
                        employeeidval.set(i[1])
                        nameval.set(pp[2])
                        mobileval.set(i[3])
                        emailval.set(pp[4])
                        addressval.set(pp[5])
                        genderval.set(pp[6])
                        salaryval.set(pp[7])
                        dateval.set(pp[8])
                        timeval.set(pp[9])
                        cityval.set(pp[10])
                            
                

        CR.mainloop()

    def showpressedemployees(Data,fireElibtnstate,quitElibtnstate,curntElibtnstate):
        cleartable()
        if len(Data)>0:
            for i in Data:
                vv=[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                employeetable.insert('',END,values=vv)
        else:
            employeetable.insert('',END,values=['None'])
        fireEbtn.config(state = fireElibtnstate)
        quitEbtn.config(state = quitElibtnstate)
        currentEbtn.config(state = curntElibtnstate)
        if Data in searchtarget:
            searchtarget.remove(Data)
        searchtarget.append(Data)
        SearchDatFunc(None)

        
    def NewFile():
        NewFile = "untitled.empl"
        root.title(NewFile)
        openedfiles.clear()
        datas.clear()
        for i in employeetable.get_children():
            employeetable.delete(i)
        filemenu.entryconfig('Save', state = 'disabled')
        filemenu.entryconfig('Save as..', state = 'normal')
        filemenu.entryconfig('New...', state = 'disabled')
        

        
    def OpenFile():
            filename = filedialog.askopenfilename(title='Open a file',initialdir='/',filetypes=[filetypes])
            if filename:
                if filename.endswith('.empl'):
                    if filename in openedfiles:
                        openedfiles.remove(filename)
                    try:
                        _file = open(filename,'rb')
                        _datas = pickle.load(_file)
                        if len(_datas) == len(datas):
                            for dat in datas:
                                if len(dat)>0:
                                    dat.clear()
                                cleartable()
                            if len(_datas[0])>0:
                                for i in _datas[0]:
                                    employeetable.insert('',END,values=i)
                                    datas[0].append(i)

                            if len(_datas[1])>0:
                                for i in _datas[1]:
                                    datas[1].append(i)
                            if len(_datas[2])>0:
                                for i in _datas[2]:
                                    datas[2].append(i)
                            if len(_datas[3])>0:
                                for i in _datas[3]:
                                    datas[3].append(i)                  

                            if len(_datas[4])>0:
                                for i in _datas[4]:
                                    datas[4].append(i)
                            if len(_datas[5])>0:
                                for i in _datas[5]:
                                    datas[5].append(i)
                            if len(_datas[6])>0:
                                for i in _datas[6]:
                                    datas[6].append(i)
                            if len(_datas[7])>0:
                                for i in _datas[7]:
                                    datas[7].append(i)

                            if len(_datas[8])>0:
                                for i in _datas[8]:
                                    datas[8].append(i)

                            fireEbtn.config(state = 'normal')
                            quitEbtn.config(state = 'normal')
                            currentEbtn.config(state = 'disabled')
                            openedfiles.append(filename)
                            FileName = filename
                            root.title(FileName)
                            filemenu.entryconfig('Save',state = 'normal')
                            filemenu.entryconfig('Save as..',state = 'disabled')
                            filemenu.entryconfig('New...', state = 'normal')
                    except EOFError:
                        messagebox.showerror('ERROR','Cant open this file because it is directly created in File explorer!')                    
                else:
                    messagebox.showerror('ERROR',"Can't open this file!\nFile must end with .empl")
    def SaveFile():
        filename = openedfiles[-1]
        _info = datas
        _file = open(filename,'wb')
        pickle.dump(_info,_file)

    def SaveFileAs():
        dirfiles=os.listdir('/')
        filename = filedialog.asksaveasfilename(title = 'Save As',initialdir = '/',filetypes=[filetypes1])
        if filename:
            if not filename.endswith('.empl'):
                filename = f'{filename}.empl'
            else:
              pass
            if filename not in dirfiles:
            
              _info = datas
              _file = open(filename,'wb')
              pickle.dump(_info,_file)

            else:
                messagebox.showerror('ERROR',str(filename)+"\n"+"File name already exist")

    def SearchDatFunc(event):
        entryval = searchval.get()
        results = []
        copyst = searchtarget[-1].copy()
        if len(searchtarget[-1])>0:
            if len(entryval)>0:
                for i in searchtarget[-1]:
                    global vv
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]

                    if(entryval in i[0] or entryval in i[1] or entryval in i[2] or entryval in i[3] or entryval in i[4] or entryval in i[5] or entryval in i[6] or entryval in i[7] or entryval in i[8] or entryval in i[9] or entryval in i[10]):
                        results.append(i)
                        copyst.remove(i)
                        copyst.append(i)
                showemployees(results)
            else:
                showemployees(searchtarget[-1])


    def showemployees(s):
        cleartable()
        if len(s)>0:
            for i in s:
                vv=[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                employeetable.insert('',END,values=vv)
        else:
            employeetable.insert('',END,values=['None'])
            
    def cleartable():
        for i in employeetable.get_children():
            employeetable.delete(i)
    def DeleteOpenedfile():
      pass

    def Savefile_and_exitWin():
      if len(openedfiles) > 0:
          if openedfiles[-1] in dirfiles:
              SaveFile()
      else:
          SaveFileAs()


    def exit_window():
        mesg=messagebox.askyesnocancel('Save?','Do You Want To Save Your Work?')
        if mesg == 1:
            Savefile_and_exitWin()
            root.destroy()
        elif mesg == 0:
            root.destroy()
        else:
            pass

    style = ttk.Style()
    style.configure('Treeview.Heading', font=('verdana', 12, 'bold'), foreground='navy blue')
    style.configure('Treeview', font=('Helvetica', 11, 'bold'), foreground='black', background='lavender')


    filetypes = (('Dat files',"*.empl"),('All files',"*.*"))
    filetypes1 = (('Dat files',"*.empl"),('All files',"*.*"))

    condition = 'None'

    curncyvals=["American Dollar", "Dollar","Euro","SAR"]
    searchtarget = []


    #All the important datas and storages

    datas = [
            [ ],
            [ ],[ ],[ ],
            [ ],[ ],[ ],[ ],
            [ ]
            ]
    quitEli = datas[1]
    fireEli = datas[2]
    quduetold = datas[3]
    fdhist=[[ ],[ ],[ ],[ ]]


    openedfiles = []#for opened files
    All_EMPL_Files = []#for All EMPL files storage
    dirfiles=os.listdir('/')
    #------------------------------------------------------------------------------------#



    for i in dirfiles:
        if i.endswith('.empl'):
            pass


    phnPatterns = ["(\d\d\d)-(\d\d\d)-(\d\d\d\d)","(\d\d\d\d\d\d\d\d\d\d)"]
    idregex = "(\d\d\d\d\d\d\d\d\d\d\d\d)"
    emplidregex = "(\d\d\d\d\d)+[A-Z]"
    Emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    winmenu = Menu(root)
    root.config(menu=winmenu)


    filemenu = Menu(winmenu, tearoff=False)
    winmenu.add_cascade(label='File',menu = filemenu)



    filemenu.add_command(label='New...', command=NewFile)
    filemenu.add_command(label='Open...', command=OpenFile)
    filemenu.add_command(label='Save', command=SaveFile)
    filemenu.add_command(label='Save as..', command=SaveFileAs)
    filemenu.add_command(label='Exit', command=exit_window)

    filemenu.entryconfig('New...', state = 'disabled')
    filemenu.entryconfig('Save',state = 'disabled')


    ShowDataFrame = Frame(root, bg='Lavender', relief=GROOVE, borderwidth=5)
    ShowDataFrame.place(x=20, y=170, width=800, height=450)

    scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
    scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)


    employeetable = Treeview(ShowDataFrame, columns=('Personal Id', 'Employee Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Salary/Month', 'Added Date', 'Added Time','City'),
                             yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=employeetable.xview)
    scroll_y.config(command=employeetable.yview)


    employeetable.heading('Personal Id', text='Personal Id')
    employeetable.heading('Employee Id', text='Employee Id')
    employeetable.heading('Name', text='Name')
    employeetable.heading('Mobile No', text='Mobile No')
    employeetable.heading('Email', text='Email')
    employeetable.heading('Address', text='Address')
    employeetable.heading('Gender', text='Gender')
    employeetable.heading('Salary/Month', text='Salary/Month')
    employeetable.heading('Added Date', text='Added Date')
    employeetable.heading('Added Time', text='Added Time')
    employeetable.heading('City', text='City')
    employeetable['show'] = 'headings'
    employeetable.column('Personal Id', width=130)
    employeetable.column('Employee Id', width=130)
    employeetable.column('Name', width=200)
    employeetable.column('Mobile No', width=130)
    employeetable.column('Email', width=220)
    employeetable.column('Address', width=120)
    employeetable.column('Gender', width=90)
    employeetable.column('Salary/Month', width=150)
    employeetable.column('Added Date', width=110)
    employeetable.column('Added Time', width=110)
    employeetable.column('City', width=120)


    employeetable.pack(fill=BOTH, expand=1)


    DataEntryFrame = Frame(root, bg="#DCAE96", bd=1, relief="groove")
    DataEntryFrame.place(x=20, y=60, width=800, height=105)

    frontlabel = Label(DataEntryFrame, text="Tools", relief="groove", bg="#f7e7ce", fg="navy blue",
                       font=("arial", 20, "bold"))
    frontlabel.pack(side="top", fill=BOTH)

    _btnframe = Frame(DataEntryFrame)
    _btnframe.pack(side='top')
    addbtn = Button(_btnframe, text="Add Employee", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                    width=12, command=addemployee)
    addbtn.pack(side='left',expand = True)

    Cbtn = Button(_btnframe, text="Command", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                       width=10, command=commandemployee)
    Cbtn.pack(side='left',expand = True)

    showinfobtn = Button(_btnframe, text="Show More info", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                       width=15, command='none')
    showinfobtn.pack(side='left',expand = True)

    btnsidef = Frame(root)
    btnsidef.pack()
    btnsidef.place(x=830,y=170)

    quitEbtn = Button(btnsidef, text="Quitted Employees", relief="raised", bg="Orange", font=("verdana", 14, "bold"), width=17,
                         command=lambda: showpressedemployees(quitEli,'normal','disabled','normal'))

    quitEbtn.pack(side='bottom',expand=True)

    fireEbtn = Button(btnsidef, text="Fired Employees", relief="raised", bg="Orange", font=("verdana", 14, "bold"), width=17,
                         command=lambda: showpressedemployees(fireEli,'disabled','normal','normal'))

    fireEbtn.pack(side='bottom',expand=True)

    currentEbtn = Button(btnsidef, text="Current Employees", relief="raised", bg="Orange", font=("verdana", 14, "bold"), width=17,
                         command=lambda: showpressedemployees(datas[0],'normal','normal','disabled'))

    currentEbtn.pack(side='bottom',expand=True)

    fsnlib = Listbox(root,width=15,height=18,font = ('time',12),bd=0,fg = '#646464',highlightthickness=0,selectbackground='#6a6a6a',activestyle='none',)

    searchval = StringVar()

    searchentry = Entry(DataEntryFrame, font=('arial', 12, 'bold'), bd=5,width = 110, textvariable = searchval)
    searchentry.pack(side='top',expand=True)

    searchentry.bind('<KeyRelease>', SearchDatFunc)

    exit_button = Button(_btnframe, text="Save And Exit", relief="raised", bg="light blue", font=("verdana", 14, "bold"), width=13, command=Savefile_and_exitWin)
    exit_button.pack(side='left',expand = True)
    main_label = Label(root, text="Employee Management System", relief="groove", bg="#FFFDD0", fg="navy blue", font=("arial", 22, "bold"))
    main_label.pack(side="top")
    clock = Label(root, font=('verdana', 10, 'bold'), relief=RAISED, borderwidth=3, bg='Lavender', fg="black")
    clock.place(x=20, y=5)

    tick()
    showpressedemployees(datas[0],fireElibtnstate='normal',quitElibtnstate='normal',curntElibtnstate='disabled')

    root.mainloop()

def login_SignUp():
    
    root = Tk()
    main(root)
    
login_SignUp()
