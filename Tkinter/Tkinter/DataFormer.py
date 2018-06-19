import RoomClass
from datetime import date
import TextFileReader
import BookingClass
import ConfigFileParser

class DataFormer:
    def FormData(jsonData,day,fileName,booking):
        TextFileReader.TextFileReader.SaveToFile(jsonData,fileName)  
        if (day):
            # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
            return DataFormer.ConvertDayJson(day,jsonData,booking)
        else:
            # Else, it returns the jsondata for the whole week
            return DataFormer.ConvertWeekJson(jsonData,booking)

    def ConvertDayJson(day,jsonData,booking):
        room = ConfigFileParser.ConfigFileParser()
        roomNumber = str(room)
        # New array of data for json
        newJsonData = []
        if(booking):
            for data in jsonData:
                if (data['WeekDay'] == date.today().isocalendar()[2]):
                    newJsonData.append(BookingClass.BookingClass(data))
            return newJsonData
        # Filters json for the day of the week.
        else:
            for data in jsonData:
                if (data['WeekDay'] == date.today().isocalendar()[2]):
                    newJsonData.append(RoomClass.Rooms(data))
            return newJsonData

    def ConvertWeekJson(jsonData,booking):
        room = ConfigFileParser.ConfigFileParser()
        roomNumber = str(room)
        # New array of data for json
        newJsonData = []

        # Filters json for the day of the week.
        if(booking):
            for data in jsonData:
                if(data['Classroom'] == roomNumber):
                    newJsonData.append(BookingClass.BookingClass(data))
            return newJsonData
        else:
            for data in jsonData:
                newJsonData.append(RoomClass.Rooms(data))
            return newJsonData


