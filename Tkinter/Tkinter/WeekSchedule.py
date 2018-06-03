import TkinterEntry
import DaySchedule as DaySchedule
import tkinter as tk
from tkinter import ttk

class scheduleWeek(tk.Frame):
    def __init__(self, master):
        # Init frame
        tk.Frame.__init__(self,master)

        # Back to dagRooster button
        button_edit = ttk.Button(self, text="Dag rooster", width=20, command=lambda:master.switch_frame(DaySchedule.scheduleDay)).grid(row=0,column=0,sticky="e")

        # Init table view
        self.init_table()

    def init_table(self):
        jsonData = TkinterEntry.RetrieveData(False)

        # Fill outer schedule : Les time + hours
        cols = 0
        rows = 0
        tk.Label(self, text=TkinterEntry.lesList[cols],font="Verdana 9 bold").grid(row=1,column=0)
        while ( cols < 5):
            tk.Label(self, text=TkinterEntry.dagList[cols],font="Verdana 9 bold").grid(row=1,column=cols + 1)
            cols = cols + 1
        while ( rows < 15):
            tk.Label(self, text=TkinterEntry.lesList[rows + 1] + "  :  " + TkinterEntry.startList[rows+ 1],font="Verdana 9 bold").grid(row=rows + 2,column=0)
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
