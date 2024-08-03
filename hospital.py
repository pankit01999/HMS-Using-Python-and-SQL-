from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class   Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold") )
        lbltitle.pack(side=TOP,fill=X)


           # Data Frame #
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",12,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)
        dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
        font=("times new roman",12,"bold"),text="Prescription")
        dataframeright.place(x=990,y=5,width=460,height=350)


          #Button Frame #
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)



        #Details  Frame #
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # DataFrame Left #
        # lblNameTablet=Label(dataframeleft,text="Names of Tablet:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet=Label(dataframeleft, font=("arial", 12, "bold"), text="Name of Tablet",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(dataframeleft,state="readonly",textvariable=self.Nameoftablets,font=("arial",12,"bold"),width=33)

        comNametablet["values"]=("Nice","Covid Vaccine","Ancetaminophen","Adderall","Amlodipne","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)  
        
        lblref=Label(dataframeleft, font=("arial", 12, "bold"), text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)     
        
        lbldose=Label(dataframeleft, font=("arial", 12, "bold"), text="Dose:",padx=2,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.Dose,width=35)
        txtdose.grid(row=2,column=1)  

        lblNoOftablets=Label(dataframeleft, font=("arial", 12, "bold"), text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.NumberofTablets, width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(dataframeleft, font=("arial", 12, "bold"), text="Lot:",padx=2,pady=6) 
        lblLot.grid(row=4, column=0,sticky=W)
        txtLot=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label (dataframeleft, font=("arial", 12, "bold"), text="Issue Date:",padx=2,pady=6) 
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(dataframeleft, font=("arial", 13, "bold"), textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(dataframeleft, font=("arial", 12, "bold"), text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataframeleft, font=("arial", 13, "bold"), textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(dataframeleft, font=("arial", 12, "bold"), text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7,column=1)
      
        lblSideEffect=Label(dataframeleft, font=("arial", 12, "bold"), text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(dataframeleft, font=("arial", 13, "bold"), textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(dataframeleft, font=("arial", 12, "bold"), text="Further Information",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.FurtherInformation, width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(dataframeleft, font=("arial", 12, "bold"), text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.DrivingUsingMachine ,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(dataframeleft, font=("arial", 12, "bold"), text="Storage Advice",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(dataframeleft, font=("arial", 12, "bold"), text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3,column=3)
        

        lblPatientId=Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(dataframeleft, font=("arial", 12, "bold"), text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(dataframeleft, font=("arial", 13, "bold"), textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)
        
        lblDateofBirth=Label(dataframeleft, font=("arial", 12, "bold"), text="Date of Birth",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.DateofBirth, width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(dataframeleft, font=("arial", 13, "bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8,column=3)


        #DataFrame Right #
        self.txtPrescription=Text(dataframeright,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
    
       # Buttons #
        btnPrescription = Button(Buttonframe, text="Prescription",bg="lightgreen",fg="black", font=("arial", 12, "bold"),width=23,padx=10, pady=1,command=self.iPreciption)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data",bg="lightgreen",fg="black", font=("arial", 12, "bold"),width=23, padx=10, pady=1,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update",bg="lightgreen",fg="black", font=("arial", 12, "bold"), width=23,padx=10, pady=1,command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete",bg="lightgreen",fg="black", font=("arial", 12, "bold"),width=23, padx=10, pady=1,command=self.idelete)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Buttonframe, text="Reset",bg="lightgreen",fg="black", font=("arial", 12, "bold"),width=23, padx=10, pady=1,command=self.clear)
        btnReset.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit",bg="lightgreen",fg="black", font=("arial", 12, "bold"),width=18, padx=10, pady=1,command=self.iExit)
        btnExit.grid(row=0, column=5)
      
      #Table#
        ##Scrollbar#
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No:")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets", text="No of tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Dailydose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")
        
        self.hospital_table["show"]="headings"
        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
      
   # Functionality Declaration #
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
             messagebox.showerror("Error", "All Fields are Required")
        else:
           conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="sHj@6378#jw", database="mydata")
           my_cur = conn.cursor()
           my_cur.execute("INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                              self.Nameoftablets.get(),
                                                                                                              self.ref.get(),
                                                                                                              self.Dose.get(),
                                                                                                              self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateofBirth.get(),
            self.PatientAddress.get()
                                                                                                               ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record Has Been Inserted")

    def update_data(self):
      conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="sHj@6378#jw", database="mydata")
      my_cur = conn.cursor()
      my_cur.execute("UPDATE hospital SET NameofTablets=%s, dose=%s, NumbersofTablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s ",
              (
              self.Nameoftablets.get(),
               self.Dose.get(),
               self.NumberofTablets.get(),
               self.Lot.get(),
               self.Issuedate.get(),
               self.ExpDate.get(),
               self.DailyDose.get(),
               self.StorageAdvice.get(),
               self.nhsNumber.get(),
               self.PatientName.get(),
               self.DateofBirth.get(),
               self.PatientAddress.get()
               ))
      conn.commit()
      conn.close()
      self.fetch_data()
      messagebox.showinfo("Success","Record Has Been Updated Successfully")                                                                                                       

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="sHj@6378#jw", database="mydata")
        my_cur = conn.cursor()
        my_cur.execute("select * from hospital")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateofBirth.set(row[11])
        self.PatientAddress.set(row[12])
    
    
    def iPreciption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Futher Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient.id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t"+self.DateofBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
         
    def idelete(self):
        conn = mysql.connector.connect(host="localhost", port=3306, username="root", password="sHj@6378#jw", database="mydata")
        my_cur = conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cur.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management system","Confirm You want to exit")
        if iExit>0:
            root.destroy()
            return
root=Tk()
ob=Hospital(root)
root.mainloop()





























