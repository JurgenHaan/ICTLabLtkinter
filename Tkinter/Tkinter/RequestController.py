import requests
import simplejson
from datetime import date
import pickle

# Hardcoded room because of *Insert reasons here*
room = "H.1.312"
class RequestController():
    def RetrieveData(day):
        try:
            #requests for data  : May take time
            request = requests
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ room + "/" + str(date.today().isocalendar()[1])
            response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})   
            jsonData = simplejson.loads(response.content)
            RequestController.SaveToFile(jsonData)
            RequestController.ReadFromFile()

            if (jsonData ==[]):
                try:
                    RequestController.ReadFromFile()
                except:
                    return []
            RequestController.SaveToFile(str(response.content))  
            if (day):
                return RequestController.ConvertJson(day,jsonData)
            else:
               return jsonData
        except:
            return []
    def ConvertJson(day,jsonData):
        # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
        newJsonData = []
        for data in jsonData:
            if (data['WeekDay'] == date.today().isocalendar()[2]):
                newJsonData.append(data)
        return newJsonData

    def SaveToFile(jsonData):
        with open("jsonRoom.txt","w") as room:
            print(jsonData)
            room.write(str(jsonData))
            room.close()
    def ReadFromFile():
        with open("jsonRoom.txt","r") as room:
            simplejson.loads(room.read())
            room.close()
