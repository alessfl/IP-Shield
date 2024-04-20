import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import datetime
import pytz

load_dotenv()

email_sender = "ipshieldsc@gmail.com"
password = os.getenv("PASSWORD")
email_reciver = "aless.flhe9@gmail.com"

timezone = pytz.timezone('America/Mexico_City')
hora_actual = datetime.datetime.now(tz=timezone)

subject = "Security Alert. (3)"
body = (f"Security Alert for aless.flhe9@gmail.com "
        "\n\nUnusual movements have been found within the learned parameters. "
        "\nSubject: Security Alert - DDoS alert to many request on instance "
        f"\n Many devices have tried to connect or generated a request in the last few minutes"
        "\n\nDetails: "
        f"\n- Date and Time: {hora_actual.strftime('%Y-%m-%d %H:%M:%S')} \nSecurity Alert for {email_reciver}\n"
        f"- User: [{email_reciver}] "
        "\n- Query Type: [Unusual network traffic] "
        "\n- Source IP: [172.28.144.228] "
        "\n\n\nImmediately contact trained security team to determine if additional action is required. "
        "\n\n\nVarious IPs may be blocked "
        "\n\n\n\n\n\nSincerely, "
        "\n[IP_Shield]")

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())
