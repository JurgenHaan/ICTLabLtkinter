import requests
import simplejson
from datetime import date

def RetrieveData(day):
    #requests for data  : May take time

    request = requests
    url = "http://acceptancetimetable2api.azurewebsites.net/api/Schedule/Lokaal/WD.02.002/" + str(date.today().isocalendar()[1])
    response = request.get(url,headers={'Authorization':'tt2', 'Accept':'application/json'})      
    jsonData = simplejson.loads(response.content)

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
