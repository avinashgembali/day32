import pandas
import datetime as dt
import random
import smtplib

EMAIL = "//gmail.com"
PASSWORD = "//"
now = dt.datetime.now()
month = now.month
day = now.day
data = pandas.read_csv("birthdays.csv")
person = ""
found = False
for index, row in data.iterrows():
    if row["day"] == day and row["month"] == month:
        found = True
        person = row["name"]
        break
if found:
    choice = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{choice}.txt", mode="r") as file:
        data = file.readlines()
    updated_lines = [line.replace("[NAME]", person) for line in data]
    with open(file=f"letter_templates/letter_{choice}.txt", mode="w") as file:
        file.writelines(updated_lines)
    with open(file=f"letter_templates/letter_{choice}.txt", mode="r") as file:
        letter_txt = file.read()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="//",
            msg=f"subject:ITS!YOUR BIRTHDAY\n\n{letter_txt}"
        )



