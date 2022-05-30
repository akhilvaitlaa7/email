from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("Email/body.html").read_text())
message = MIMEMultipart()
message["from"] = "Akhil Vaitla"
message["to"] = "testpythonmail22@gmail.com"
message["subject"] = "This is a test mail"
body = template.substitute({"name": "Akhil"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(
    Path("Email/car.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testpythonmail22@gmail.com", "testmail22")
    smtp.send_message(message)
    print("Sent....")
