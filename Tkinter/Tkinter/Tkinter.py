import tkinter as tk
from tkinter import ttk
import requests
import simplejson


# Dummy Day data
lesList = ["Les uur","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
startList = ["Start","8:30","9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]
docentList = ["Docent","OMARA", "OMARA","","OMARA","", "","OMARA","OMARA","OMARA", "OMARA","OMARA","","OMARA", "OMARA",""]
klasList = ["Klas","INF3A", "INF3A","","INF3A","", "","INF3A","INF3A","INF3A", "INF3A","INF3A","","INF3A", "INF3A",""]
vakList = ["Vak","INFLAB01","INFLAB01","","INFLAB01","","","INFLAB01","INFLAB01","INFLAB01","INFLAB01","INFLAB01","","INFLAB01","INFLAB01",""]
lesList2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
startList2 = ["8:30","9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]

# Dummy Week Data
dagList = ["Maandag", "Dinsdag", "Woensdag","Donderdag","Vrijdag"]

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
        # Init frame
        tk.Frame.__init__(self,parent)

        # Sets selected item to none
        self.selected_item = None
        self.parent = parent
        self.controller = controller

        # Inits the buttons and pictures
        self.init_buttons(self.controller)

        # Builds foundation of the treeview
        self.Build_Treeview(self.parent,self.controller)

    def Build_Treeview(self, parent,controller): 
        # Init treeview
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

        # Requests for data  : May take time
        request = requests
        url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Lokaal/WN.02.007/22"
        response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})        
        jsonData = simplejson.loads(response.content)
        newJsonData = []

        # Checks for weekdays  - we only want 1 day
        for data in jsonData:
            if (data['WeekDay'] == 3):
                newJsonData.append(data)

        # Fill treeview
        n = 1
        while(n != 16):
            if (newJsonData == []):
                break
            for data in newJsonData:
                b = 0
                if ( data['StartBlock'] == n):
                    while (data['StartBlock'] + b < data['EndBlock']+ 1):
                        self.tv.insert("","end",text = "",values = (n + b,startList[n + b], data['Teacher'], data['Class'], data['CourseCode']))
                        b = b + 1
            if (b == 0):
                self.tv.insert("","end",text = "",values = (n,startList[n],"","",""))
                n = n + 1
            else:
                n = n + b

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

    def Destroy(self):
        self.update()

    def init_buttons(self,controller):
        # Load images 
        HROlogo = tk.PhotoImage(file="./Images/HRO.png")
        QRcode = tk.PhotoImage(file="./Images/QRcode.png")
        iname = tk.Canvas(bg="black",height=80,width=80)
        iname.pack()

        imageQR = iname.create_image(700,50,anchor="n",image=QRcode)
        imageHR= iname.create_image(700,30,anchor="n",image=HROlogo)

        HROpicture = ttk.Label(self,image=HROlogo).grid(row = 0, column=9,sticky="W")
        QRpicture = ttk.Label(self,image=QRcode)

        # Pictures and everything
        ttk.Label(self,text="De kamer temperatuur is: " + str(temperatuur)+ " graden.").grid(row= 0, column=7,sticky="W")
        ttk.Button(self, text = "Reserveer kamer", width=20, command=lambda:self.reserve_room(self.selected_item)).grid(row=0, column=3, sticky="W")
        ttk.Button(self, text="Week rooster", width=20, command=lambda:controller.show_frame(scheduleWeek)).grid(row=0,column=1,sticky="W")
        ttk.Button(self, text = "Verwijder reservering", width=25, command=lambda:self.delete_reservation()).grid(row=0, column=5, sticky="W")


class scheduleWeek(tk.Frame):
    def __init__(self, parent,controller):
        # Init frame
        tk.Frame.__init__(self,parent)

        # Back to dagRooster button
        button_edit = ttk.Button(self, text="Dag rooster", width=20, command=lambda:controller.show_frame(scheduleDay)).grid(row=0,column=0,sticky="e")

        # Init table view
        self.init_table()

    def init_table(self):

        # Requests for data  : May take time
        request = requests
        url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Lokaal/WN.02.007/22"
        response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})        
        jsonData = simplejson.loads(response.content)

        # Fill outer
        cols = 0
        rows = 0
        tk.Label(self, text=lesList[cols]).grid(row=1,column=0)
        while ( cols < 5):
            tk.Label(self, text=dagList[cols]).grid(row=1,column=cols + 1)
            cols = cols + 1
        while ( rows < 15):
            tk.Label(self, text=lesList[rows + 1] + "  :  " + startList[rows+ 1]).grid(row=rows + 2,column=0)
            rows = rows + 1

        # Fill inner schedule
        cols = 1
        while ( cols < 6):
            if (jsonData == []):
                break
            rows = 2
            while (rows < 17):
                b = 0
                for data in jsonData:
                    if (data['WeekDay'] == cols and data['StartBlock'] == rows - 1):
                        while (data['StartBlock'] + b < data['EndBlock']+ 1):
                            tk.Label(self, text=str(data['Class']) + " "  + str(data['Teacher']) + " " + str(data['CourseCode'])).grid(row=rows + b,column=cols )
                            b = b + 1
                if (b == 0):
                    tk.Label(self, text="       ").grid(row=rows,column=cols)
                    rows = rows + 1
                else:
                    rows = rows + b
            cols = cols + 1

# Tkinter loop
roosterMain = scheduleMainScreen()
roosterMain.title("Room signing")
roosterMain.geometry("1280x900")
while True:
    roosterMain.update()