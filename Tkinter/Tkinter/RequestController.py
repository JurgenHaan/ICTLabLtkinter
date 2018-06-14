import requests
import simplejson
from datetime import date
import json
import base64
import tkinter as tk

# Hardcoded room because of *Insert reasons here*
room = "WD.02.016"

class RequestController():
    def RetrieveData(day):
        try:
            #requests for data  : May take time
            request = requests
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ room + "/" + str(date.today().isocalendar()[1])
            response = request.get(url,headers = {'Authorization': 'Basic ' + str(base64.b64encode(bytes("Pi:WD.02.016","utf8")))[1:].strip("'")})   
            jsonData = simplejson.loads(response.content)
            return RequestController.FormData(jsonData,day)
        except:
            try:
                return RequestController.FormData(RequestController.ReadFromFile(),day)
            except:
                return ["Lost"]

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
            print(dataset)
            return simplejson.loads(dataset)

