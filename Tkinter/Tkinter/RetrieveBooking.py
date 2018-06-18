import requests
import ConfigFileParser
import base64
import json
import RequestController
import DataFormer
import TextFileReader
from datetime import date

class RetrieveBooking:
    def RetrieveBookingData(day,booking):
        try:
            #requests for data  : May take time
            request = requests
            room = ConfigFileParser.ConfigFileParser()
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/MyBookings/"+ str(date.today().isocalendar()[1])
            authString = str(base64.b64encode(bytes("Pi:" + str(room),"utf8")))
            print(authString[1:].strip("'"))
            response = request.get(url,headers = {'Authorization': 'Basic ' + authString[1:].strip("'")})  
            jsonData = json.loads(response.content)
            print(response.content)
            return DataFormer.DataFormer.FormData(jsonData,day,"jsonBooking.txt",booking)
        except:
            try:
                return DataFormer.DataFormer.FormData(TextFileReader.TextFileReader.ReadFromFile("jsonBooking.txt"),day,"jsonBooking.txt",booking)
            except:
                return ["Lost"]