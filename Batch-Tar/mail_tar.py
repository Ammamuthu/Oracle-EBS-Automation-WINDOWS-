import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email setup
smtpServer = '' #Your smtp 
smtpPort = 587  # Port for TLS
fromAddr = '' #Sender address
paswrd = '' #Your sender password

# Recipients
toAddrList = [] #Reciver address / You can give mutiple address like ' ',' ',' '

# Email content
subject = "Tar Backup done - 16 server"
body = "Tar backup is done on 16 server .\n\n\nBest regards,\nAmmamuthu"

# Create a MIME multipart message
msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = ', '.join(toAddrList)
msg['Subject'] = subject

# Attach body as plain text
msg.attach(MIMEText(body, 'plain'))

# Create SMTP connection
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(fromAddr, paswrd)

# Send email
server.sendmail(fromAddr, toAddrList, msg.as_string())

# Quit SMTP session
server.quit()
