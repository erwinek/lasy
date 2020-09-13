'''
import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.wp.pl", port, context=context) as server:
    server.login("erwinek@wp.pl", password)
    # TODO: Send email here
    
    sender_email = "erwinek@wp.pl"
    receiver_email = "leszek.kula@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    # Send email here
    
    server.sendmail(sender_email, receiver_email, message)
'''
    
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "erwinek@wp.pl"
receiver_email = "leszek.kula@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = "text"

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
#part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
#message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.wp.pl", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )