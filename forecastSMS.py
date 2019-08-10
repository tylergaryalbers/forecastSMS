from twilio.rest import Client
from darksky import forecast

# use darkskylib API wrapper to call forecast / weather attributes of specific coordinates, API key first, the lat/long
weather = forecast('<darksky api key>',<latitude>, <longtitude>)
windbearing = weather.windBearing
windspeed = weather.windSpeed
temp = weather.temperature
forecast = weather.summary

# function to turn wind bearing mumber into standard readable wind direction
def windcompass(windbearing):
    val = int((windbearing/22.5)+.5)
    argument = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return argument[(val % 16)]

direction = windcompass(windbearing)

#message for text
smsbody = f'The wind is blowing {direction} at {windspeed} MPH. It is {temp} degrees outside and it is currently {forecast}.'
#print statement for debugging text in console
print(smsbody)

# function for sending sms - uses twilio to send an sms to specified number
def forecastSMS():
    client = Client("<Twiilio account SID", "Twilio auth token")
    message = client.messages.create(to="<recipient number", from_="<given Twiliio phone #", body=smsbody)
forecastSMS()
