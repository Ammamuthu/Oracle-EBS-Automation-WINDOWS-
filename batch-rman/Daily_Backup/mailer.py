import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time

# Email setup
smtpServer = '' #Your smtp 
smtpPort = 587  # Port for TLS
fromAddr = '' #Sender address
toAddr_list = [] #Reciver address / You can give mutiple address like ' ',' ',' '
paswrd = '' #Your sender password

# Function to send email with log file attachment
def send_email_with_attachment(file_path, toAddr):
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['Subject'] = 'Tar Backup completed'

    with open(file_path, 'r') as file:
        body = file.read()

    msg.attach(MIMEText(body, 'plain'))

    # Attach the log file
    attachment = MIMEText(body)
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
    msg.attach(attachment)

    # Connect to SMTP server and send email
    server = smtplib.SMTP(smtpServer, smtpPort)
    server.starttls()
    server.login(fromAddr, paswrd)
    server.sendmail(fromAddr, toAddr, msg.as_string())
    server.quit()

# Assuming the log file is generated with the name 'backup_daily_prod_<date>.log'
log_file_name = f"backup_daily_prod_{time.strftime('%m_%d_%Y')}.log"
log_file_path = os.path.join('D:', 'Automation-scripts', 'Batch-scripts', log_file_name)

# Check if the log file exists and send email if found
if os.path.exists(log_file_path):
    for toAddr in toAddr_list:
        send_email_with_attachment(log_file_path, toAddr)
else:
    print("Log file not found.")
