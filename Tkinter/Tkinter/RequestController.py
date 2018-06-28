import requests
from datetime import date
import simplejson
import base64
import ConfigFileParser
import RoomClass
import TextFileReader
import DataFormer

class RetrieveRooms():
    def RetrieveData(day,booking,endPoint):
        try:

            #requests for data  : May take time
            request = requests
            endPointString = "http://acceptancetimetable2api.azurewebsites.net/api/" + endPoint
            room = ConfigFileParser.ConfigFileParser()
            url = endPointString + str(room) + "/" + str(date.today().isocalendar()[1])
            authString = str(base64.b64encode(bytes("Pi:" + str(room),"utf8")))
            response = request.get(url,headers = {'Authorization': 'Basic ' + authString[1:].strip("'")})   
            jsonData = simplejson.loads(response.content)
            if(endPoint == "Schedule/Classroom/"):
                return DataFormer.DataFormer.FormData(jsonData,day,"jsonRoom.txt",booking)
            else:
                return DataFormer.DataFormer.FormData(jsonData,day,"jsonBooking.txt",booking)
        except:
            if(endPoint == "Schedule/Classroom/"):
                try:
                    return DataFormer.DataFormer.FormData(TextFileReader.TextFileReader.ReadFromFile("jsonRoom.txt"),day,"jsonRoom.txt",booking)
                except:
                    return ["Lost"]
            else:
                try:
                    return DataFormer.DataFormer.FormData(TextFileReader.TextFileReader.ReadFromFile("jsonBooking.txt"),day,"jsonBooking.txt",booking)
                except:
                    return ["Lost"]
