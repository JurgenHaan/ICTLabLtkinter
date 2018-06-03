import tkinter as tk
import requests
import simplejson
from datetime import date
import DaySchedule as daySchedule
import WeekSchedule as weekSchedule

# Dummy Day data
lesList = ["Les uur","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
startList = ["Start","8:30","9:20", "10:30","11:20","12:10","13:00","13:50","15:00","15:50", "17:00", "17:50", "18:40", "19:30", "20:20","21:10"]

# Dummy Week Data
dagList = ["Maandag", "Dinsdag", "Woensdag","Donderdag","Vrijdag"]

# Dummy temp data.
# Data opvragen van sensor
temperatuur = 21

def RetrieveData(day):
    #requests for data  : May take time

    request = requests
    url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Lokaal/WN.02.007/" + str(date.today().isocalendar()[1])
    response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})        
    jsonData = simplejson.loads(response.content)

    # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
    if (day == True):
        newJsonData = []
        for data in jsonData:
            if (data['WeekDay'] == date.today().isocalendar()[2]):
                newJsonData.append(data)
        return newJsonData
    else:
        #Returns Weekschedule
        return jsonData

class scheduleMainScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(daySchedule.scheduleDay)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

# Tkinter loop
if __name__ == "__main__":
    roosterMain = scheduleMainScreen()
    roosterMain.geometry("900x500")
    roosterMain.title("Room signing")
    roosterMain.mainloop()
    
