import pyowm
api_key = "f77e4effca3aad14aae25fb4a551daa1"   
City = input("Enter City Name: ")
owm_obj=pyowm.OWM(api_key)
mgr = owm.weather_manager()
obs = mgr.weather_at_place(City)
weather=obs.weather
temp = weather.temperature()['temp']
hum = weather.humidity
desc = weather.status
print("Source = weathermap, City =",City,", Temperature=",temp,", Humidity =",hum,", description =",desc)
