import DaySchedule as DaySchedule
import tkinter as tk
from tkinter import ttk
import RequestController as req
from PIL import Image,ImageTk
import ConfigFileParser
import RetrieveBooking
import grovepi

class scheduleWeek(tk.Frame):
    def __init__(self, master):
        # Init frame
        tk.Frame.__init__(self,master)
        try:
            self.temperatuur = grovepi.dht(4,0)
        self.room = ConfigFileParser.ConfigFileParser()
        self.dagList = ["Maandag", "Dinsdag", "Woensdag","Donderdag","Vrijdag"]
        self.lesList = ["Les uur / Tijd ","1 ","2 ","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        self.startList = ["Start"," 8:30"," 9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]
        self.master = master

        self.init_buttons()
        # Init table view
        self.Fill_outer()

        self.Fill_inner()
    def Fill_outer(self):
        # Fill outer schedule : Les time + hours
        cols = 0
        rows = 0

        tk.Label(self, text=self.lesList[cols],font="Verdana 10 bold").grid(row=1,column=0)
        while ( cols < 5):
            tk.Label(self, text=self.dagList[cols],font="Verdana 10 bold").grid(row=1,column=cols + 1)
            cols = cols + 1
        while ( rows < 15):
            tk.Label(self, text=self.lesList[rows + 1] + "  :  " + self.startList[rows+ 1],font="Verdana 10 bold").grid(row=rows + 2,column=0)
            rows = rows + 1

    def Fill_inner(self):
        # Retrieve data
        jsonData = req.RetrieveRooms.RetrieveData(False,False)
        bookingData = RetrieveBooking.RetrieveBooking.RetrieveBookingData(False,True)
        # Fill inner schedule
        cols = 1
        while ( cols < 6):
            if (jsonData == ["Lost"] or bookingData == ["Lost"]):
                ttk.Label(self,text="Lost connection to server",font="Verdana 12 bold").grid(row=8, column=3)
                break
            rows = 2
            while (rows < 17):
                b = 0
                for data in jsonData:
                    if (data.WeekDay == cols and data.StartBlock == rows - 1):
                        while (data.StartBlock + b < data.EndBlock + 1):
                            tk.Label(self, text=str(data.Classes[0]['Name']) + " "  + str(data.Teacher) + " " + str(data.CourseCode),font="Verdana 9").grid(row=rows + b,column=cols )
                            b = b + 1
                for data in bookingData:
                    if (data.WeekDay == cols and data.StartBlock == rows - 1):
                        while (data.StartBlock + b < data.EndBlock + 1):
                            tk.Label(self, text=str("Gereserveerd"),font="Verdana 9").grid(row=rows + b,column=cols )
                            b = b + 1
                if (b == 0):
                    tk.Label(self, text="").grid(row=rows,column=cols)
                    rows = rows + 1
                else:
                    rows = rows + b
            cols = cols + 1

    def init_buttons(self):
        # HRO image load
        logo = ImageTk.PhotoImage(Image.open("./Images/HRO.png"))
        HROpicture = ttk.Label(self,image=logo)
        HROpicture.image = logo
        HROpicture.grid(row= 0, column=0)

        # Back to day schedule button
        ttk.Button(self, text="Dag rooster", width=20,padding= 5, command=lambda:self.master.switch_frame(DaySchedule.scheduleDay)).grid(row=0,column=1)

        # Refresh screen button - if information might have changed
        ttk.Button(self, text="Refresh", width=20,padding= 5, command=lambda:self.master.switch_frame(scheduleWeek)).grid(row=0,column=2)

        ttk.Label(self,text="De temperatuur in lokaal "+ str(self.room) +" is: \n" + str(self.temperatuur)+ " graden.",font="Verdana 9 bold").grid(row= 0, column=3)
        
