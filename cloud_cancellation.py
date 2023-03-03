import pycookiecheat
import requests
import re
from bs4 import BeautifulSoup as beaty
import smtplib
from email.message import EmailMessage


class CloudCancellation:
    def __init__(self, cancelling, reason=None, success=None):
        self.cancelling = cancelling
        self.reason = reason
        self.success = success

    def server_cancellation(self):
        existing_cloud = False
        self.cancelling = ''.join(re.findall(r'c\d+.***.net', self.cancelling))
        if self.cancelling:
            existing_cloud = True
        if existing_cloud:
            self.reason = input('Reason for cancellation + TID#: ')
        else:
            print('Incorrect Cloud')
        maco_url = 'https://***/'
        cancellation_url = 'https://***'
        cookies = pycookiecheat.chrome_cookies(
                maco_url,
                cookie_file='/Users/galin.velikov/Library/Application Support/Google/Chrome/Profile 1/Cookies')
        payload = {'location': self.cancelling, 'reason': self.reason, 'hours_until_cancellation': '48'}
        response = requests.post(cancellation_url, data=payload, cookies=cookies).text
        output = beaty(response, "html.parser").find("div", {"class": "CoolErrorDiv"})
        print(f'\n{output.text.strip()}')
        if 'successfully' in output.text.strip():
            cloud_cancellation.email_sending()

    def email_sending(self):
        body = f"The monitoring was disabled for the server {self.cancelling} and added for cancellation due to {self.reason}\n" \
               "\nBest Regards,\n" \
               "\nGalin Velikov" \
               "\nSystem Administrator" \
               "\n***"
        sender_email = "g***@****.com"
        password = 'trollface'
        msg = EmailMessage()
        msg.set_content(body)

        msg['Subject'] = f'Monitoring disabled for cloud {self.cancelling}'
        msg['From'] = "Galin Velikov"
        msg['To'] = "s***@***.com"
        msg['cc'] = "g***@**.com"
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, password)
            server.send_message(msg)
            server.quit()
            print("Successfully sent email")
        except Exception as ex:
            print("Something went wrong brat … check it further", ex)


cloud = input('Cloud for cancellation: ')
cloud_cancellation = CloudCancellation(cloud)
cloud_cancellation.server_cancellation()
