import requests
import simplejson
from datetime import date
import json
import base64
import tkinter as tk

# Hardcoded room because of *Insert reasons here*
room = "H.1.110"
class Rooms:
    def __init__(self,jsondata):
        self.Id = jsondata["Id"]
        self.Week = jsondata["WeekDay"]
        self.StartBlock = jsondata["StartBlock"]
        self.EndBlock = jsondata["EndBlock"]
        self.Teacher = jsondata["Teacher"]
        self.Description = jsondata["Description"]
        self.CourseCode = jsondata["CourseCode"]
        print(jsondata["Classes"])
        if(len(jsondata['Classes']) >= 1):
            self.Classes = jsondata["Classes"]
        else:
            self.Classes = [{"Name": "None"}]
        self.Rooms = jsondata["Rooms"]

class RequestController():
    def RetrieveData(day):
        try:
            #requests for data  : May take time
            request = requests
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ room + "/" + str(date.today().isocalendar()[1])
            response = request.get(url,headers = {'Authorization': 'Basic ' + str(base64.b64encode(bytes("Pi:" + room,"utf8")))[1:].strip("'")})   
            jsonData = simplejson.loads(response.content)
            newJsonData = []
            return RequestController.FormData(jsonData,day)
        except:
            try:
                return RequestController.FormData(RequestController.ReadFromFile(),day)
            except:
                return ["Lost"]

    def FormData(jsonData,day):
        RequestController.SaveToFile(jsonData)  
        if (day):
            # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
            return RequestController.ConvertDayJson(day,jsonData)
        else:
            # Else, it returns the jsondata for the whole week
            return RequestController.ConvertWeekJson(jsonData)

    def ConvertDayJson(day,jsonData):

        # New array of data for json
        newJsonData = []

        # Filters json for the day of the week.
        for data in jsonData:
            if (data['WeekDay'] == date.today().isocalendar()[2]):
                newJsonData.append(Rooms(data))
        return newJsonData

    def ConvertWeekJson(jsonData):

        # New array of data for json
        newJsonData = []

        # Filters json for the day of the week.
        for data in jsonData:
            newJsonData.append(Rooms(data))
        return newJsonData


    def SaveToFile(jsonData):
        with open("jsonRoom.txt","w") as room:
            #Dumps the JSON to the jsonRoom.txt file
            json.dump(jsonData,room)

            room.close()

    def ReadFromFile():
        with open("jsonRoom.txt") as room:
            #Retrieve data from txt file and transform it into a string
            dataset = str(room.readlines())

            # For some reason, there an extra [' in front and behind the string. This takes it off for JSON
            dataset = dataset[2:]
            dataset = dataset[:len(dataset)-2]

            #Returns the JSON
            return simplejson.loads(dataset)

