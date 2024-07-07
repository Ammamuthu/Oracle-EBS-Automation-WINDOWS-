import smtplib

smtpServer = '121.243.77.117'
smtpPort = 587  # Port for TLS
fromAddr = 'ammamuthu.m@3i-infotech.com'
toAddr = 'ammamuthu.m@3i-infotech.com'
text = "This is a test of sending email from within Python."

# Create an SMTP object and initiate the TLS connection
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()

# Login to the SMTP server with your Gmail credentials
server.login('ammamuthu.m@3i-infotech.com', 'Aura@123')

# Send the email
server.sendmail(fromAddr, toAddr, text)

# Quit the SMTP session
server.quit()
