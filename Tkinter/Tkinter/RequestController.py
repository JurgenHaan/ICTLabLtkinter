import requests
import simplejson
from datetime import date
import json
import base64
import ConfigFileParser
import RoomClass
import TextFileReader

class RequestController():
    def RetrieveData(day):
        try:
            #requests for data  : May take time
            request = requests
            room = ConfigFileParser.ConfigFileParser()
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ str(room) + "/" + str(date.today().isocalendar()[1])
            response = request.get(url,headers = {'Authorization': 'Basic ' + str(base64.b64encode(bytes("Pi:" + str(room),"utf8")))[1:].strip("'")})   
            jsonData = simplejson.loads(response.content)
            return RequestController.FormData(jsonData,day)
        except:
            try:
                return RequestController.FormData(TextFileReader.TextFileReader.ReadFromFile(),day)
            except:
                return ["Lost"]

    def FormData(jsonData,day):
        TextFileReader.TextFileReader.SaveToFile(jsonData)  
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
                newJsonData.append(RoomClass.Rooms(data))
        return newJsonData

    def ConvertWeekJson(jsonData):

        # New array of data for json
        newJsonData = []

        # Filters json for the day of the week.
        for data in jsonData:
            newJsonData.append(RoomClass.Rooms(data))
        return newJsonData

