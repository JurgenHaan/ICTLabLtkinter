import WeekSchedule as weekSchedule
import FrameController as frameController
import RequestController as req
import ConfigFileParser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import RetrieveBooking
import grovepi

class scheduleDay(tk.Frame):
    def __init__(self, master):
        # Init frame
        tk.Frame.__init__(self,master)
        [temp,hum] = grovepi.dht(4,0)
        self.temp = 21
        self.room = ConfigFileParser.ConfigFileParser()
        self.startList = ["Start"," 8:30"," 9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]
        # Sets selected item to none
        self.selected_item = None

        # Creates variable for the master class FrameController
        self.master = master

        # Inits the buttons and pictures
        self.init_buttons()

        # Builds foundation of the treeview
        self.Build_Treeview(self.master)

    def Build_Treeview(self,master): 
        # Init treeview
        self.tv = ttk.Treeview(self,  height=15)
        self.tv['columns'] = ('lesuur', 'start', 'docent', 'klas', 'vak')
        self.tv.heading("#0", text='')
        self.tv.column("#0", stretch="NO", width=1)
        self.tv.heading('lesuur', text='Les uur')
        self.tv.column('lesuur', anchor='center', width=100)
        self.tv.heading('start', text='Tijd stip')
        self.tv.column('start', anchor='center', width=150)
        self.tv.heading('docent', text='Leraar')
        self.tv.column('docent', anchor='center', width=150)
        self.tv.heading('klas', text='Klas')
        self.tv.column('klas', anchor='center', width=150)
        self.tv.heading('vak', text='Vak')
        self.tv.column('vak', anchor='center', width=200)
        self.tv.bind('<ButtonRelease-1>', self.select_item) 
        self.tv.grid(row=1, column=0, columnspan=20, padx=0, pady=20)

        ttk.Style().configure("Treeview", font= ('Verdana', 12), background="#383838", 
        foreground="white", fieldbackground="grey")

        self.Fill_Treeview()

    def Fill_Treeview(self):
        # Requests for data  : May take time
        jsonData = req.RetrieveRooms.RetrieveData(True,False)
        bookingData = RetrieveBooking.RetrieveBooking.RetrieveBookingData(False,True)
        # Fill treeview
        n = 1
        while(n != 16):
            if (jsonData == ["Lost"] and bookingData == ["Lost"]):
                ttk.Label(self,text="Lost connection to server",font="Verdana 12 bold").grid(row= 3, column=0)
                break
            b = 0
            if(jsonData != []):
                for data in jsonData:
                    if ( data.StartBlock == n):
                        while (data.StartBlock + b < data.EndBlock + 1):
                            self.tv.insert("","end",text = "",values = (n + b,self.startList[n + b], data.Teacher, data.Classes[0]['Name'], data.CourseCode))
                            b = b + 1
            if(bookingData != [] and bookingData != ['Lost'] ):
                for data in bookingData:
                    if (data.StartBlock == n):
                        while (data.StartBlock + b < data.EndBlock + 1):
                            self.tv.insert("","end",text = "",values = (n + b,self.startList[n + b], "Geboekt", " Student",""))
                            b = b + 1
            if (b == 0 or jsonData == []):
                self.tv.insert("","end",text = "",values = (n,self.startList[n],"","",""))
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


    def init_buttons(self):

        # Load images 
        logo = ImageTk.PhotoImage(Image.open("./Images/HRO.png"))
        HROpicture = ttk.Label(self,image=logo)
        HROpicture.image = logo
        HROpicture.grid(row= 0, column=0)

        # Pictures and everything
        ttk.Button(self, text="Week rooster", width=20,padding= 5, command=lambda:self.master.switch_frame(weekSchedule.scheduleWeek)).grid(row=0,column=1)
        
        ttk.Button(self, text="Refresh", width=20, padding= 5, command=lambda:self.master.switch_frame(scheduleDay)).grid(row=0,column=2)
        
        ttk.Label(self,text="De temperatuur in lokaal "+ str(self.room) +" is: \n" + str(self.temp)+ " graden.",font="Verdana 9 bold").grid(row= 0, column=3)

        #Options for reserving - NOT USED BUT MAYBE FOR IN THE FUTURE OR EXTRA'S
        #ttk.Button(self, text = "Reserveer kamer", width=20, command=lambda:self.reserve_room(self.selected_item)).grid(row=0, column=5, sticky="W")
        #ttk.Button(self, text = "Verwijder reservering", width=25, command=lambda:self.delete_reservation()).grid(row=0, column=7, sticky="W")
