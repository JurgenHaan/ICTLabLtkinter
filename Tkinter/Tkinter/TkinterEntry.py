import tkinter as tk
import time
import FrameController


# Dummy Day data
lesList = ["Les uur / Tijd ","1 ","2 ","3","4","5","6","7","8","9","10","11","12","13","14","15"]
startList = ["Start"," 8:30"," 9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]

# Dummy Week Data
dagList = ["Maandag", "Dinsdag", "Woensdag","Donderdag","Vrijdag"]


# Dummy temp data.
# Data opvragen van sensor
temperatuur = 21

# Tkinter loop
if __name__ == "__main__":
    roosterMain = FrameController.scheduleMainScreen()
    roosterMain.geometry("1280x720")
    roosterMain.title("Room signing")
    roosterMain.mainloop()