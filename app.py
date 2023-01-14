import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
recip_list = []

def send_out(subject, content_file, recipient_file, sender_email):
    '''
    This function sends emails based on parameters using the SendGrid API.

    Parameters:
    subject (str)
    content_file (str of file name)
    recipient_file (str of file name)
    sender_email (str)

    Prints response status/headers
    '''

    from_email = Email(sender_email)  
    text_content = ""

    with open(content_file) as f1:
        for line in f1.readlines():
            text_content += line
    
    with open(recipient_file) as f2:
        for line in f2.readlines():
            recip_list.append(line)
            to_email = To(line) 
            content = Content("text/plain", text_content)
            mail = Mail(from_email, to_email, subject, content)

            # Get a JSON-ready representation of the Mail object
            mail_json = mail.get()             

            # Send an HTTP POST request to /mail/send
            response = sg.client.mail.send.post(request_body=mail_json)
            print(response.status_code)
            print(response.headers)

    
send_out("ok", "/Users/lucastucker/sg_quickstart/content_file.txt", 
"/Users/lucastucker/sg_quickstart/recip.txt", "png@gmail.com")
