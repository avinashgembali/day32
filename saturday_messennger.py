import smtplib
import random
import datetime as dt

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 5:
    my_email = "//@gmail.com"
    password = "//"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        with open(file="quotes.txt", mode="r") as file:
            data = file.read()
            quotes = data.split("\n")
        msg_to_sent = random.choice(quotes)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anyemailofother",
            msg=f"subject:quotes\n\n{msg_to_sent}"
        )

