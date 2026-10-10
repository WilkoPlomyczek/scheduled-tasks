##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict()
print(birthdays)

now = dt.datetime.now()
for x in birthdays["month"]:
    if birthdays["month"][x] == now.month and birthdays["day"][x] == now.day:
        with open(f"letter_templates/letter_{random.choice([1,2,3])}.txt", mode="r") as letter:
            name = birthdays["name"][x]
            text = letter.read()
            text = text.replace("[NAME]", f"{name}")
            print(text)
# AFTER (secrets stored securely in GitHub)
        my_email = os.environ.get("MY_EMAIL")
        password = os.environ.get("MY_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com", 587, local_hostname="localhost") as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="aniawilkosz@hotmail.com",
                                msg=f"Subject:Happy birthday!\n\n {text}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




