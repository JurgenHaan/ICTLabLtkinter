import requests
import simplejson
from datetime import date

# Hardcoded room because of *Insert reasons here*
room = "H.1.312"

def RetrieveData(day):
    #requests for data  : May take time
    request = requests
    try:
        url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Lokaal/"+ room + "/" + str(date.today().isocalendar()[1])
        response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})      
        jsonData = simplejson.loads(response.content)
    except:
        return []
    # If the Day schedule is requesting data, we only want 1 day - Checks if it for day schedule
    if (day == True):
        newJsonData = []
        for data in jsonData:
            if (data['WeekDay'] == date.today().isocalendar()[2]):
                newJsonData.append(data)
        return newJsonData
    else:
        #Returns Weekschedule
        return jsonData
