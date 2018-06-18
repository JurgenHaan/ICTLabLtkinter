import unittest
import RoomClass
import ConfigFileParser
import RequestController
import BookingClass
import TextFileReader
from datetime import date

class RoomClassTest(unittest.TestCase):
    def test_ConvertJsonStringToRoomClass(self):
        Json = {"Id": "59ca7e3f-68bb-11e8-8697-525400c8e11c", "Week": 24, "WeekDay": 2, "StartBlock": 1, "EndBlock": 4, "Teacher": "AMMMQ", "Description": "SKC gesprekken", "CourseCode": None, "Classes": [], "Rooms": [{"RoomId": "H.1.114", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.306", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.312", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.315", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.110", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.112", "Capacity": 99, "Maintenance": 0}]}
        room = RoomClass.Rooms(Json)
        self.assertEqual(room.Classes,[{"Name": "None"}])
        self.assertEqual(room.CourseCode,Json["CourseCode"])
        self.assertEqual(room.Description,Json["Description"])
        self.assertEqual(room.EndBlock,Json["EndBlock"])
        self.assertEqual(room.Rooms[0],Json["Rooms"][0])
        self.assertEqual(room.StartBlock,Json["StartBlock"])
        self.assertEqual(room.Teacher,Json["Teacher"])
        self.assertEqual(room.Week,Json["Week"])
        self.assertEqual(room.WeekDay,Json["WeekDay"])

    def test_configFileReader(self):
        config = ConfigFileParser.ConfigFileParser()
        self.assertEqual("H.1.318",str(config))

    def test_ConvertJsonStringToBookingClass(self):
        Json = {"Id": "fe789bfe-72da-11e8-a825-525400c8e11c", "Type": 0, "EndBlock": 3, "StartBlock": 1, "Guests": 1, "Classroom": "H.2.318", "WeekDay": 3, "Week": 25}
        bookedRoom = BookingClass.BookingClass(Json)
        self.assertEqual(bookedRoom.Id, Json["Id"])
        self.assertEqual(bookedRoom.Classroom, Json["Classroom"])
        self.assertEqual(bookedRoom.EndBlock, Json["EndBlock"])
        self.assertEqual(bookedRoom.StartBlock, Json["StartBlock"])
        self.assertEqual(bookedRoom.Guests, Json["Guests"])
        self.assertEqual(bookedRoom.Type, Json["Type"])
        self.assertEqual(bookedRoom.Week, Json["Week"])
        self.assertEqual(bookedRoom.WeekDay, Json["WeekDay"])

    def test_SaveToTextFileAndReadItAgain(self):
        old_stuff = TextFileReader.TextFileReader.ReadFromFile("jsonRoom.txt")

        new_stuff = [{"Id": "59ca7e3f-68bb-11e8-8697-525400c8e11c", "Week": date.today().isocalendar()[1], "WeekDay": 2, "StartBlock": 1, "EndBlock": 4, "Teacher": "AMMMQ", "Description": "SKC gesprekken", "CourseCode": None, "Classes": [], "Rooms": [{"RoomId": "H.1.114", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.306", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.312", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.315", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.110", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.112", "Capacity": 99, "Maintenance": 0}]}]
        TextFileReader.TextFileReader.SaveToFile(new_stuff,"jsonRoom.txt")
        new_stuff_check = TextFileReader.TextFileReader.ReadFromFile("jsonRoom.txt")
        self.assertEqual(new_stuff,new_stuff_check)
        TextFileReader.TextFileReader.SaveToFile(old_stuff,"jsonRoom.txt")