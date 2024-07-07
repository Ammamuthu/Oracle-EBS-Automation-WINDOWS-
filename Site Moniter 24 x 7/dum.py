# import time
# import requests
# import logging
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Log File setup
# logging.basicConfig(filename='Web_status.log', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
# log = []

# # Mail setup
# smtpServer = '121.243.77.117'
# smtpPort = 587  # Port for TLS
# fromAddr = 'ammamuthu.m@3i-infotech.com'
# # toAddr = 'ammamuthu2001@gmail.com'
# paswrd = 'BattleisON@22'

# to_adres_lst =['ammamuthu.m@3i-infotech.com' ,'hudson.s@3i-infotech.com', 'ARUNKUMAR.S@3i-infotech.com', 'john.h@3i-infotech.com']
# server = smtplib.SMTP(smtpServer, smtpPort)
# server.starttls()
# server.login(fromAddr, paswrd)

# # Actual setup
# def check_website_status(websites):
#     html_content = ""  # Initialize outside of the if block

#     for website in websites:
#         try:
#             response = requests.get(website)

#             if response.status_code == 200:
#                 logging.warning(f"{website} is alive (Status Code: {response.status_code})")
#             elif response.status_code == 500:
#                 message = f"{website} returned a 500 Internal Server Error\n{response.text}"
#                 log.append(message)
#                 logging.warning(message)
#             else:
#                 message = f"{website} returned an unexpected status code: {response.status_code}"
#                 log.append(message)
#                 logging.warning(message)
#         except requests.RequestException as e:
#             error_message = f"{website} is not reachable. Exception: {e}"
#             logging.warning(error_message)
#             log.append(error_message)

#     # Check if there are any issues and send an email
#     if log:
#         email_subject = "Website Status Alert"
#         email_body = "\n".join(log)
#         # Create a MIMEText object to include HTML content
#         html_content = f"""
#         <html>
#             <body>
#                 <header style="color:White; font-weight:bolder;">Website is Down</header>
#                 <tr><p style="color:black; font-weight:bold;">{email_body}</p></tr>
#             </body>
#         </html>
#         """
    
#     for to_email in to_adres_lst:
#         email_message = MIMEMultipart()
#         email_message.attach(MIMEText(html_content, 'html', 'utf-8'))
#         email_message['Subject'] = email_subject
#         email_message['From'] = fromAddr
#         email_message['To'] = to_email

#         server.sendmail(fromAddr, to_email, email_message.as_string())
#         print(f"MAIL SENT to {to_email}....")

#     print(log)
#     log.clear()

# while True:
#     # List of websites to check
#     websites_to_check = [
#         "http://erpuat.najrancement.local:8012/OA_HTML/AppsLogin",    # 17 server
#         "http://erptest.najrancement.local:8012/OA_HTML/AppsLogin",   # 16 server -R12.2.10
#         "http://erpdev.najrancement.local:8000/"                     # 78 server
#        # "http://erpdev.najrancement.local:8028/",                     # 16 server iteration2
#     ]

#     # Run the check
#     check_website_status(websites_to_check)
#     logging.warning("......................................")

#     print("Executing the script...")
#     time.sleep(900)

# server.quit()


import time
import requests
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Log File setup
logging.basicConfig(filename='Shed.log', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = []

# Mail setup
smtpServer = '121.243.77.117'
smtpPort = 587  # Port for TLS
fromAddr = 'ammamuthu.m@3i-infotech.com'
# toAddr = 'ammamuthu2001@gmail.com'
paswrd = 'BattleisON@22'

to_adres_lst =['ammamuthu.m@3i-infotech.com']
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(fromAddr, paswrd)
# Actual setup
def check_website_status(websites):
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
        email_subject = "Website Status Alert"
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

while True:
    # List of websites to check
    websites_to_check = [
        "https://www.google.com",
        "http://erpuat.najrancement.local:8012/OA_HTML/AppsLogin",    # 17 server
        "http://erptest.najrancement.local:8012/OA_HTML/AppsLogin",   # 16 server -R12.2.10
        "http://erpdev.najrancement.local:8000/",                     # 78 server
        "http://erpdev.najrancement.local:8028/",                     # 16 server iteration2
    ]

    # Run the check
    check_website_status(websites_to_check)
    logging.warning("......................................")

    print("Executing the script...")
    time.sleep(100)

server.quit()
