# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import pandas as pd
import smtplib as s
import datetime as dt
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD)

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


# from datetime import datetime
# import pandas
# import random
# import smtplib
# import os

# # import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
