import json
from datetime import date
class TextFileReader:
    def SaveToFile(jsonData):
        with open("jsonRoom.txt","w") as room:
            #Dumps the JSON to the jsonRoom.txt file
            json.dump(jsonData,room)

            room.close()

    def ReadFromFile():
        with open("jsonRoom.txt") as room:
            #Retrieve data from txt file and transform it into a string
            dataset = str(room.readlines())

            # For some reason, there an extra [' in front and behind the string. This takes it off for JSON conversion
            dataset = dataset[2:]
            dataset = dataset[:len(dataset)-2]

            #Returns the JSON
            dataset = json.loads(dataset)
            verifyData = dataset[0]
            if(date.today().isocalendar()[1] != verifyData['Week']):
                raise Exception("Lost!")
            return dataset


