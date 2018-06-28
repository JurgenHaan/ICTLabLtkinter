import json
from datetime import date

class TextFileReader:
    def SaveToFile(jsonData,fileName):
        with open(fileName,"w") as room:
            #Dumps the JSON to the jsonRoom.txt file
            json.dump(jsonData,room)

            room.close()

    def ReadFromFile(fileName):
        with open(fileName) as room:
            #Retrieve data from txt file and transform it into a string
            dataset = str(room.readlines())       
            print(dataset)
            # For some reason, there an extra [' in front and behind the string. This takes it off for JSON conversion
            dataset = dataset[2:]
            dataset = dataset[:len(dataset)-2]
            try:
            #Returns the JSON
                dataset = json.loads(dataset)
                verifyData = dataset[0]
                print(verifyData)
                if(date.today().isocalendar()[1] != verifyData['Week']):
                    raise Exception("Lost!")
                return dataset
            except:
                raise Exception("Lost!")


