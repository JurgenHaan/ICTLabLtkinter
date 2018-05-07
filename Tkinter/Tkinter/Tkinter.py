import tkinter as tk
from tkinter import ttk

# Dummy Day data
lesList = ["Les uur","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
startList = ["Start","8:30","9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]
docentList = ["Docent","OMARA", "OMARA","","OMARA","", "","OMARA","OMARA","OMARA", "OMARA","OMARA","","OMARA", "OMARA",""]
klasList = ["Klas","INF3A", "INF3A","","INF3A","", "","INF3A","INF3A","INF3A", "INF3A","INF3A","","INF3A", "INF3A",""]
vakList = ["Vak","INFLAB01","INFLAB01","","INFLAB01","","","INFLAB01","INFLAB01","INFLAB01","INFLAB01","INFLAB01","","INFLAB01","INFLAB01",""]

# Dummy Week Data
maandagList = ["Maandag", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "", "", ""]
dinsdagList = ["Dinsdag", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "", "", ""]
woensdagList = ["Woensdag", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "", "", "", ""]
donderdagList = ["Donderdag", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "", "", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "", "", ""]
vrijdagList = ["Vrijdag", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "", "INF3C MINUA INFLAB01", "INF3C MINUA INFLAB01", "", "", "", ""]

#List of week list
weekList = [maandagList,dinsdagList,woensdagList,donderdagList,vrijdagList]

#List of day list
dayList = [lesList,startList,docentList,klasList,vakList]

# Dummy temp data.
# Data opvragen van sensor
temperatuur = 21

# Meh font
LARGE_FRONT= ("Verdana",9)

class scheduleMainScreen(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand= True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames= {}

        for F in (scheduleDay,scheduleWeek):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(scheduleDay)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class scheduleDay(tk.Frame):
    def __init__(self, parent,controller):
        self.selected_item = None
        self.Build_Treeview(parent,controller)

    def Build_Treeview(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.init_buttons(controller)   
        self.tv = ttk.Treeview(self,  height=15)
        self.tv['columns'] = ('lesuur', 'start', 'docent', 'klas', 'vak')
        self.tv.heading("#0", text='', anchor='w')
        self.tv.column("#0", stretch="NO", width=5, anchor="w")
        self.tv.heading('lesuur', text='Les uur')
        self.tv.column('lesuur', anchor='center', width=100)
        self.tv.heading('start', text='Tijd stip')
        self.tv.column('start', anchor='center', width=150)
        self.tv.heading('docent', text='Leraar')
        self.tv.column('docent', anchor='center', width=150)
        self.tv.heading('klas', text='Klas')
        self.tv.column('klas', anchor='center', width=150)
        self.tv.heading('vak', text='Vak')
        self.tv.column('vak', anchor='center', width=150)
        self.tv.bind('<ButtonRelease-1>', self.select_item) 
        self.tv.grid(row=1, column=0, columnspan=15, padx=5, pady=5)
        self.treeview = self.tv
        
        ttk.Style().configure("Treeview", font= ('', 11), background="#383838", 
        foreground="white", fieldbackground="yellow")
        self.Fill_Treeview()
    def Fill_Treeview(self):
        self.tv.insert("","end",text = "",values = ("1","8.30", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("2","9.20", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("3","10.30", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("4","11.20", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("5","12.10", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("6","13.00", "", "", ""))
        self.tv.insert("","end",text = "",values = ("7","13.50", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("8","15.00", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("9","15.50", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("10","17.00", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("11","17.50", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("12","18.40", "OMARA", "INF3A", "INFLAB01"))
        self.tv.insert("","end",text = "",values = ("13","19.30", "", "", ""))
        self.tv.insert("","end",text = "",values = ("14","20.20", "", "", ""))
        self.tv.insert("","end",text = "",values = ("15","21.10", "", "", ""))

        
    def select_item(self,a):
        try:
            item = self.tv.selection()[0]
            self.selected_item = item
            print(self.selected_item)
        except:
            print("Nothing selected :/")
        
    def reserve_room(self,selected):
        try:
            item = self.tv.selection()[0]
        except:
            print("Nothing selected :/")
        if selected == None or self.tv.item(selected)['values'][2] != "":
            print("Too bad")
        elif (self.tv.item(selected)['values'][2] == ""): 
            value= self.tv.item(selected)['values']
            self.tv.item(selected,values=(value[0],
                                      value[1],
                                      "Student gereserveerd",
                                      "Student gereserveerd",
                                      "Zelf studie"))

    def delete_reservation(self):
        try:
            item = self.tv.selection()[0]
        except:
            print("Nothing selected :/")
        if (self.tv.item(item)['values'][2] == "Student gereserveerd"):
            value= self.tv.item(item)['values']
            self.tv.item(item,values=(value[0],
                                      value[1],
                                      "",
                                      "",
                                      ""))
        else:
            print("Too bad")

    def init_buttons(self,controller):
        HROlogo = tk.PhotoImage(file="./Images/HRO.png")
        QRcode = tk.PhotoImage(file="./Images/QRcode.png")
        iname = tk.Canvas(bg="black",height=80,width=80)
        iname.pack()
        imageQR = iname.create_image(700,50,anchor="n",image=QRcode)
        imageHR= iname.create_image(700,30,anchor="n",image=HROlogo)
        HROpicture = ttk.Label(self,image=HROlogo).grid(row = 0, column=9,sticky="W")
        QRpicture = ttk.Label(self,image=QRcode)

        ttk.Label(self,text="De kamer temperatuur is: " + str(temperatuur)+ " graden.").grid(row= 0, column=7,sticky="W")
        ttk.Button(self, text = "Reserveer kamer", width=20, command=lambda:self.reserve_room(self.selected_item)).grid(row=0, column=3, sticky="W")
        ttk.Button(self, text="Week rooster", width=20, command=lambda:controller.show_frame(scheduleWeek)).grid(row=0,column=1,sticky="W")
        ttk.Button(self, text = "Verwijder reservering", width=25, command=lambda:self.delete_reservation()).grid(row=0, column=5, sticky="W")

     

class scheduleWeek(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        button_edit = ttk.Button(self, text="Dag rooster", width=20, command=lambda:controller.show_frame(scheduleDay)).grid(row=0,column=0,sticky="e")
        self.init_table()
    def init_table(self):
        rows = 1
        cols = 0
        for F in (weekList):
            for X in (F):
                tk.Label(self, text=X).grid(row=rows,column=cols)
                rows = rows + 1
            rows = 1
            cols = cols + 1

roosterMain = scheduleMainScreen()
roosterMain.title("Room signing")
roosterMain.geometry("800x600")
roosterMain.mainloop()