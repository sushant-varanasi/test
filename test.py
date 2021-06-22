import requests
api_key='505a498a2378ea1162c895a5d7c87c25'
location=input("enter the city name: ")
complete_api_link=("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key)

print(complete_api_link)
print("\n")

api_link=requests.get(complete_api_link)
api_data=api_link.json()

print(api_data)

print("\n")
temp_city=((api_data['main']['temp'])-273.15)

print("temp city: " + str(temp_city))

print("\n")
print("\n")
print("\n")


weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']


print("----------------------------------------------------")
print(" weather stats for {} ".format(location.upper()))
print("----------------------------------------------------")
print(" current temperature is:{:.2f} deg C".format(temp_city))
print("current weather desc :",weather_desc)
print("current humidity  :",hmdt,'%')
print(" current wind speed  :",wind_speed,'kmph')

#location2 = "rr" + location + "hh"

strigg = "----------------------------------------------------" + "\nweather stats for " + location.upper() + "\n----------------------------------------------------"+ "\ncurrent temperature is:{:.2f} deg C".format(temp_city) + "\ncurrent weather desc :" + weather_desc + "\ncurrent humidity  :" + str(hmdt) + "%" + "\ncurrent wind speed  :" + str(wind_speed) + "kmph"

f = open("demofile2.txt", "w")
f.write(strigg)
f.close()

