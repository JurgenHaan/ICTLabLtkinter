class Rooms:
    def __init__(self,jsondata):
        self.Id = jsondata["Id"]
        self.Week = jsondata["Week"]
        self.WeekDay = jsondata["WeekDay"]
        self.StartBlock = jsondata["StartBlock"]
        self.EndBlock = jsondata["EndBlock"]
        self.Teacher = jsondata["Teacher"]
        self.Description = jsondata["Description"]
        self.CourseCode = jsondata["CourseCode"]
        if(len(jsondata['Classes']) >= 1):
            self.Classes = jsondata["Classes"]
        else:
            self.Classes = [{"Name": "None"}]
        self.Rooms = jsondata["Rooms"]