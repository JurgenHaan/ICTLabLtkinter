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
            authString = str(base64.b64encode(bytes("Pi:" + str(room),"utf8")))
            url = "http://acceptancetimetable2api.azurewebsites.net/api/Booking/Bookings/"+str(room)+"/"+ str(date.today().isocalendar()[1])
            response = request.get(url,headers = {'Authorization': 'Basic ' + authString[1:].strip("'")})   
            jsonData = json.loads(response.content)
            return DataFormer.DataFormer.FormData(jsonData,day,"jsonBooking.txt",booking)
        except:
            try:
                return DataFormer.DataFormer.FormData(TextFileReader.TextFileReader.ReadFromFile("jsonBooking.txt"),day,"jsonBooking.txt",booking)
            except:
                return ["Lost"]