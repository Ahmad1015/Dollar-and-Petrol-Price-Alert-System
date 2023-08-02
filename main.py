import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests


def send_email(rate, message, previous):
    _ = load_dotenv()
    email_address_from = os.environ.get("send_email_from")
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_address_to = os.environ.get("send_email_to")
    if not email_address_to or not email_password or not email_address_from:
        raise ValueError("Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")

    # create email
    msg = EmailMessage()
    msg['Subject'] = message
    msg['From'] = email_address_from
    msg['To'] = email_address_to
    msg.set_content(
        f"Dollar Rate dropped down to {rate} from previous {previous}. The difference is of {previous - rate}")

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address_from, email_password)
        smtp.send_message(msg)


def dollar_rate():
    global previous_dollar_rate
    dollar_response = requests.get("https://www.google.com/search?q=1+dollar+to+pkr").text
    soup = BeautifulSoup(dollar_response, "html.parser")
    rate = soup.find(name="div", class_="BNeawe iBp4i AP7Wnd").getText().strip()
    try:
        float_rate = float(rate[0:6])
    except ValueError:
        float_rate = float(rate[0:5])

    if float_rate < previous_dollar_rate:
        send_email(float_rate, "Dollar Rate Update", previous_dollar_rate)
        dollar_file = open("dollar_rate.txt", "w")
        dollar_file.write(str(float_rate))


previous_petrol_price = previous_dollar_rate = 0


def petrol_price():
    global previous_petrol_price
    petrol_response = requests.get("https://www.psopk.com/").text
    soup2 = BeautifulSoup(petrol_response, "html.parser")
    rate = soup2.find(name="div", class_="uk-width-auto").getText().strip()
    try:
        float_rate = float(rate[3:9])
    except ValueError:
        float_rate = float(rate[3:8])

    if float_rate < previous_petrol_price:
        send_email(float_rate, "Petrol Price Update", previous_petrol_price)
        petrol_file = open("petrol_rate.txt", "w")
        petrol_file.write(str(float_rate))


def set_globals():
    global previous_dollar_rate, previous_petrol_price
    dollar_file = open("dollar_rate.txt", "r")
    previous_dollar_rate = float(dollar_file.readline())
    petrol_file = open("petrol_rate.txt", "r")
    previous_petrol_price = float(petrol_file.readline())



def main():
    set_globals()
    petrol_price()
    dollar_rate()
    print("Program successfully executed")


if __name__ == "__main__":
    main()
