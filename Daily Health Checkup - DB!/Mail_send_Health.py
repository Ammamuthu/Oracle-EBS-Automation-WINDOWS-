import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import os
import time

# Email setup
smtpServer = '' #Your smtp 
smtpPort = 587  # Port for TLS
fromAddr = '' #Sender address
toAddr_list = [] #Reciver address / You can give mutiple address like ' ',' ',' '
paswrd = '' #Your sender password

# Function to send email with HTML file attachment
def send_email_with_attachment(file_path, toAddr):
  msg = MIMEMultipart()
  msg['From'] = fromAddr
  msg['To'] = toAddr
  msg['Subject'] = 'Health-Check-PROD !'

  body = "Hi \n\nThis is a Database Status of Prod , You can see the attached HTML report for detailed information \n\nThanks and Regards,\nAmmamuthu M. \n[+91 *********I*]"  # Optional plain text body

  msg.attach(MIMEText(body, 'plain'))

  # Attach the HTML file
  with open(file_path, 'rb') as file:  # Open in binary mode
      html_content = file.read()
  attachment = MIMEBase('text', 'html')  # Specify attachment type as HTML
  attachment.set_payload(html_content)
  attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
  msg.attach(attachment)

  # Connect to SMTP server and send email
  server = smtplib.SMTP(smtpServer, smtpPort)
  server.starttls()
  server.login(fromAddr, paswrd)
  server.sendmail(fromAddr, toAddr, msg.as_string())
  server.quit()

# Assuming the HTML file name follows the format
log_file_name = f"HEALTH_CHECKUP_{time.strftime('%Y_%m_%d')}.html"
base_dir = r"F:\Automation\DUMP\Health_Checkup"
log_file_path = os.path.join(base_dir, log_file_name)

print(log_file_path)

# Check if the log file exists and send email if found
if os.path.exists(log_file_path):
  for toAddr in toAddr_list:
    send_email_with_attachment(log_file_path, toAddr)
    print(f"Email sent successfully to {toAddr}")
else:
  print("Log file not found.")
