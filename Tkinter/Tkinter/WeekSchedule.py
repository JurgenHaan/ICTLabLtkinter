import TkinterEntry
import DaySchedule as DaySchedule
import tkinter as tk
from tkinter import ttk
import RequestController as req
from PIL import Image,ImageTk

class scheduleWeek(tk.Frame):
    def __init__(self, master):
        # Init frame
        tk.Frame.__init__(self,master)

        self.master = master

        self.init_buttons()
        # Init table view
        self.Fill_outer()

<<<<<<< HEAD
        self.Fill_inner()
=======
>>>>>>> master
    def Fill_outer(self):
        # Fill outer schedule : Les time + hours
        cols = 0
        rows = 0

        tk.Label(self, text=TkinterEntry.lesList[cols],font="Verdana 10 bold").grid(row=1,column=0)
        while ( cols < 5):
            tk.Label(self, text=TkinterEntry.dagList[cols],font="Verdana 10 bold").grid(row=1,column=cols + 1)
            cols = cols + 1
        while ( rows < 15):
            tk.Label(self, text=TkinterEntry.lesList[rows + 1] + "  :  " + TkinterEntry.startList[rows+ 1],font="Verdana 10 bold").grid(row=rows + 2,column=0)
            rows = rows + 1
        self.Fill_inner()

    def Fill_inner(self):
        # Retrieve data
        jsonData = req.RequestController.RetrieveData(False)

    def Fill_inner(self):
        # Retrieve data
        jsonData = req.RequestController.RetrieveData(False)

        # Fill inner schedule
        cols = 1
        while ( cols < 6):
            if (jsonData == ["Lost"]):
                ttk.Label(self,text="Lost connection to server",font="Verdana 12 bold").grid(row=17, column=1)
                break
            rows = 2
            while (rows < 17):
                b = 0
                for data in jsonData:
                    if (data['WeekDay'] == cols and data['StartBlock'] == rows - 1):
                        while (data['StartBlock'] + b < data['EndBlock']+ 1):
                            if(len(data["Classes"]) >= 1):
                                tk.Label(self, text=str(data['Classes'][0]['Name']) + " "  + str(data['Teacher']) + " " + str(data['CourseCode']),font="Verdana 9").grid(row=rows + b,column=cols )
                                b = b + 1
                            else:
                                tk.Label(self, text="None "  + str(data['Teacher']) + " " + str(data['CourseCode']),font="Verdana 9").grid(row=rows + b,column=cols )
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

        ttk.Label(self,text="Welkom in lokaal "+ req.room,font="Verdana 9 bold").grid(row= 0, column=3)
        
