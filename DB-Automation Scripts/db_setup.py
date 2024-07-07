import subprocess
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule

logging.basicConfig(filename='Db_status.log', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = []

# Mail setup
smtpServer = '' #Your smtp 
smtpPort = 587  # Port for TLS
fromAddr = '' #Sender address
paswrd = '' #Your sender password

to_adres_lst = #Reciver address / You can give mutiple address like ' ',' ',' '
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(fromAddr, paswrd)


def check_database_status(hostname, port, service_name):
    # Construct the TNS entry
    tns_entry = f'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})))'

    # Use tnsping to check the status
    command = f'tnsping {tns_entry}'

    try:
        subprocess.run(command, check=True, shell=True)
        logging.warning(f"The database on {hostname}:{port}/{service_name} is UP.")
    except subprocess.CalledProcessError as e:
        err = f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}"
        logging.warning(err)
        print(err)
        log.append(err)
        print(len(log))

# Create a MIMEText object to include HTML content (defined outside of if log:)
    html_content = ""

# Check if there are any issues and send an email
    if log:
        email_subject = "Database Status Alert"
        email_body = "\n".join(log)
        # Create a MIMEText object to include HTML content
        html_content = f"""
        <html>
            <body>
            <header style="color:White; font-weight:bolder;">Website is Down</header>
            <tr><p style="color:black; font-weight:bold;">{email_body}</p></tr>
            </body>
        </html>
        """
        for to_email in to_adres_lst:
            email_message = MIMEMultipart()
            email_message.attach(MIMEText(html_content, 'html', 'utf-8'))
            email_message['Subject'] = email_subject
            email_message['From'] = fromAddr
            email_message['To'] = to_email

            server.sendmail(fromAddr, to_email, email_message.as_string())
            print(f"MAIL SENT to {to_email}....")

    print(log)
    log.clear()

logging.warning('.....................................')
print("Executing the script...")

# Example usage
database = [{"hostname": "localhost", "port": "1521", "service_name": "xe"},
            {"hostname": "Your_server_ip", "port": "Db_port", "service_name": "demo"}]


def job():
    for db in database:
        check_database_status(db["hostname"], db["port"], db["service_name"])


# Schedule the job every 1 minute
schedule.every(1).minutes.do(job)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
