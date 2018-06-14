import requests
import simplejson
from datetime import date
import pickle
import json

# Hardcoded room because of *Insert reasons here*
room = "WD.02.016"
class RequestController():
    def RetrieveData(day):
          #requests for data  : May take time
        request = requests
        url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ room + "/" + str(date.today().isocalendar()[1])
        response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})   
        jsonData = simplejson.loads(response.content)
        if(response.status_code ==200 or jsonData == []):
            return RequestController.FormData(jsonData,day)
        else:
            try:
                return RequestController.FormData(RequestController.ReadFromFile(),day)
            except:
                return []

    def FormData(jsonData,day):
        RequestController.SaveToFile(jsonData)  
        if (day):
            return RequestController.ConvertJson(day,jsonData)
        else:
            return jsonData

    def ConvertJson(day,jsonData):
        # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
        newJsonData = []
        for data in jsonData:
            if (data['WeekDay'] == date.today().isocalendar()[2]):
                newJsonData.append(data)
        return newJsonData

    def SaveToFile(jsonData):
        with open("jsonRoom.txt","w") as room:
            json.dump(jsonData,room)
            room.close()

    def ReadFromFile():
        with open("jsonRoom.txt") as room:
            dataset = str(room.readlines())
            dataset = dataset[2:]
            dataset = dataset[:len(dataset)-2]
            return simplejson.loads(dataset)

