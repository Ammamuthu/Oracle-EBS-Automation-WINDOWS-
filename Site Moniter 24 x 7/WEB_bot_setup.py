import requests
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Log File setup
logging.basicConfig(filename='F:\Automation\DUMP\Website_Alert\APP_Status.log', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = []

# Mail setup
smtpServer = '' #Your smtp 
smtpPort = 587  # Port for TLS
fromAddr = '' #Sender address
paswrd = '' #Your sender password

to_adres_lst = [] #Reciver address / You can give mutiple address like ' ',' ',' '
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(fromAddr, paswrd)

# Actual setup
def check_website_status(websites):
    html_content = ""  # Initialize with an empty string
    email_subject = "Website Status Alert"  # Default subject

    for website in websites:
        try:
            response = requests.get(website)

            if response.status_code == 200:
                logging.warning(f"{website} is alive (Status Code: {response.status_code})")
            elif response.status_code == 500:
                message = f"{website} returned a 500 Internal Server Error\n{response.text}"
                log.append(message)
                logging.warning(message)
            else:
                message = f"{website} returned an unexpected status code: {response.status_code}"
                log.append(message)
                logging.warning(message)
        except requests.RequestException as e:
            error_message = f"{website} is not reachable. Exception: {e}"
            logging.warning(error_message)
            log.append(error_message)

    # Check if there are any issues and send an email
    if log:
        email_body = "\n".join(log)
        # Create a MIMEText object to include HTML content
        html_content = f"""
        <html>
            <body>
                <header style="color:White; font-weight:bolder;">Website is Down</header>
                <p> You can find the Log for more information about website in side a server 17</p>
                <h5>'F:\Automation\DUMP\Website_Alert\APP_Status.log'<\h5>
                <br>
                
                <tr><p style="color:black; font-weight:bold;">{email_body}</p></tr>
                
                <br><br>
                "\n\nThanks and Regards,
                <br>
                \nAmmamuthu M. 
                <br>
                \n[+91 ******************]"
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

while True:
    # List of websites to check
    websites_to_check = [
        "https://www.youtube.com/",
        "https://www.Google.com/"
        
    ]

    # Run the check
    check_website_status(websites_to_check)
    logging.warning("......................................")

    print("Executing the script...")
    time.sleep(60 * 60)

server.quit()
