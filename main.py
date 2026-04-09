import os
import requests
from twilio.rest import Client
OPEN_WM = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters={
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url= OPEN_WM, params= parameters)
response.raise_for_status()
weather_data = response.json()
shall_rain = False

for hour_data in weather_data ["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        shall_rain = True
if shall_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Hey MBgeniuS, \n\nIt's going to rain today. Don't leave home without your jacket 🧥 or umbrella ☔",
        to="whatsapp:+447424957521"
    )
    print(message.status)






