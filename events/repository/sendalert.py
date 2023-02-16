"""import smtplib
import ssl
from email.mime.text import MIMEText



# Setup port number and servr name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

sender = "shailesh.cs20@bitsathy.ac.in"
recipients = ['shailesh20034@gmail.com', 'shaileshshailu002@gmail.com']
pswd = "hojvgjecntollmxk"
# content of message

msg = MIMEText("bodsdfndfj n y")
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)

# Create context
simple_email_context = ssl.create_default_context()
try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(sender, pswd)
    print("Connected to server :-)")

    # Send the actual email
    print()
    print(f"Sending email to - {recipients}")
    TIE_server.sendmail(sender, recipients, msg.as_string())
    print(f"Email successfully sent to - {recipients}")
# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()
"""
def sendMail(date,session,mail_list=[]):
    print("sending mail to",mail_list)