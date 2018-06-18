class BookingClass:
    def __init__(self,jsondata):
        self.Id = jsondata["Id"]
        self.Week = jsondata["Week"]
        self.WeekDay = jsondata["WeekDay"]
        self.StartBlock = jsondata["StartBlock"]
        self.EndBlock = jsondata["EndBlock"]
        self.Guests = jsondata["Guests"]
        self.Classroom = jsondata["Classroom"]
        self.Type = jsondata["Type"]