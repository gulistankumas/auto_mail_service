import smtplib
import random
import datetime as dt


MY_EMAİL="your mail"
MY_PASSWORD="your pass"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("auto_mail\quotes.txt","r") as notes:
        all_quotes= notes.readlines()
        quote=random.choice(all_quotes)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAİL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAİL, 
        to_addrs=["member email1","member email2"] ,
        msg=f"Subject:weekly mood booster is here!\n\n{quote}")
