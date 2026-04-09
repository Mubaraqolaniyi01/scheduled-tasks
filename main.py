import os
# import pandas as pd
# import smtplib as s
# import datetime as dt
# import random

# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# now = dt.datetime.now()
# today_tuple = (now.month, now.day)
#  # Limited to 1 person
# data = pd.read_csv("birthdays.csv")
# birthday_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthday_dict:
#     celebrant = birthday_dict[today_tuple]
#     file_path = f"letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", celebrant["name"])  # To avoid not replacing the [NAME], we redefine the variable

#     with s.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=celebrant["email"],
#             msg=f"Subject: Birthday Heralds\n\n{contents}"
#         )
#         print(f"Email sent successfully to {celebrant["name"]}")
#_________________________________________________________
import requests
from twilio.rest import Client
OPEN_WM = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID)")
auth_token = os.environ.get("AUTH_TOKEN")

parameters={
    "lat": 4.771490,
    "lon": 7.014350,
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
        body="It's going to rain today. Remember to bring an ☔",
        to="whatsapp:+447424957521"
    )
    print(message.status)






