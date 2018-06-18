import requests
from datetime import date
import json
import base64
import ConfigFileParser
import RoomClass
import TextFileReader
import DataFormer

class RetrieveRooms():
    def RetrieveData(day,booking):
        try:

            #requests for data  : May take time
            request = requests
            room = ConfigFileParser.ConfigFileParser()
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Classroom/"+ str(room) + "/" + str(date.today().isocalendar()[1])
            authString = str(base64.b64encode(bytes("Pi:" + str(room),"utf8")))
            response = request.get(url,headers = {'Authorization': 'Basic ' + authString[1:].strip("'")})   
            jsonData = json.loads(response.content)

            return DataFormer.DataFormer.FormData(jsonData,day,"jsonRoom.txt",booking)
        except:
            try:
                return DataFormer.DataFormer.FormData(TextFileReader.TextFileReader.ReadFromFile("jsonRoom.txt"),day,"jsonRoom.txt",booking)
            except:
                return ["Lost"]