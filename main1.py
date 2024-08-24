# import smtplib
#
# my_email = "//@gmail.com"
# password = "****"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="///any email of other",
#         msg="subject:hello\n\nhi avinash."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.weekday()
# for 0 it means it is monday and for sunday it is 6
dob = dt.datetime(year=2004, month=9, day=11)
print(dob)