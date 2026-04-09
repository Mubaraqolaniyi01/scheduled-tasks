import os
import pandas as pd
import smtplib as s
import datetime as dt
import random

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today_tuple = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    celebrant = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", celebrant["name"])  # To avoid not replacing the [NAME], we redefine the variable

    with s.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=celebrant["email"],
            msg=f"Subject: Birthday Heralds\n\n{contents}"
        )
        print(f"Email sent successfully to {celebrant["name"]}")
