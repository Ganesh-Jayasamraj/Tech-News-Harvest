import smtplib, ssl, os
from dotenv import load_dotenv, find_dotenv
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from firebase import fetch_usermails

load_dotenv(find_dotenv())
Sender_mail_id = os.environ.get('Sender_Mail_id')
Sender_Password = os.environ.get('Senders_Password')

def get_message_content():
    with open("./Generated_Files/News-Stack.html", 'r') as file:
        message_content = ""
        message_content += str(file.read())
        file.close()
    return message_content

def send_email():
    try:
        sender = Sender_mail_id
        receivers = fetch_usermails()

        smtp_server = "smtp-mail.outlook.com"
        port = 587

        password = Sender_Password

        todate = date.today().strftime("%d-%m-%y")

        message_body = MIMEMultipart()
        message_body['Subject'] = f"{todate}'s TECH NEWS"

        context = ssl.create_default_context()
        server = smtplib.SMTP(host=smtp_server, port=port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(user=sender, password=password)

        message_body.attach(MIMEText(get_message_content(), "html"))
        server.sendmail(sender, receivers, message_body.as_string())
        print("Mail Sent Successfully, Check your mail box and Spam too")

    except Exception as exp:
        print(exp)

    finally:
        server.quit()

if __name__ == "__main__":
    send_email()
    get_message_content()