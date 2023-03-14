import numpy as np
from django.conf import settings
import os


def get_weather(month, day):  
    table_loc = os.path.join(settings.BASE_DIR,"dndsite", "static", 'files', "DnDTABLE.csv")
    result = np.genfromtxt(table_loc,dtype=None,encoding=None, delimiter = ",")
    for i in range(len(result)):
        if month in result[i][0]:
            if day == result[i][1]:
                temp = result[i][2] + (np.random.randint(-5,5))
                precip = np.random.choice(2,p=[0.75,0.25])
                wind_strength = np.random.randint(0,5)
                if result[i][3] == "n/a":
                    sunrise = 0
                    sunset = 0
                    if result[i][5] == "24":
                        daylight = "all day"
                    else:
                        daylight = "all night"                        
                else:
                    sunrise = result[i][3]
                    sunset = result[i][4]
                    daylight = result[i][5]
                if precip:
                    precip_strength = np.random.randint(1,5)     
                    temp -= precip_strength  
                    if temp <= 0: 
                        precip = 0
                        snow = 1
                        temp -= (precip_strength + wind_strength)
                    else:
                        snow = 0
                else:
                    snow=0
                break
    print("On ",month,",",day," it will be ", temp, "degrees" )
    if sunrise:
        print("Sunrise will be at:", sunrise)
        print("Sunset will be at:", sunset)
        print("There will be", daylight, "of daylight")
    else:
        print(daylight)
    
    if precip: 
        print("it is raining with strength", precip_strength)  
    if snow: 
       print("it is snowing with strength", precip_strength)  
        
    print("the wind speed today is", wind_strength)    

    return