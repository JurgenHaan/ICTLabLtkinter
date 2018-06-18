import unittest
import RoomClass
import ConfigFileParser
import RequestController

class RoomClassTest(unittest.TestCase):
    def test_ConvertJsonStringToRoomClass(self):
        Json = {"Id": "59ca7e3f-68bb-11e8-8697-525400c8e11c", "Week": 24, "WeekDay": 2, "StartBlock": 1, "EndBlock": 4, "Teacher": "AMMMQ", "Description": "SKC gesprekken", "CourseCode": None, "Classes": [], "Rooms": [{"RoomId": "H.1.114", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.306", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.312", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.315", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.110", "Capacity": 99, "Maintenance": 0}, {"RoomId": "H.1.112", "Capacity": 99, "Maintenance": 0}]}
        room = RoomClass.Rooms(Json)
        self.assertEqual(room.Classes,[{"Name": "None"}])

    def test_configFileReader(self):
        config = ConfigFileParser.ConfigFileParser()
        self.assertEqual("H.1.318",str(config))
