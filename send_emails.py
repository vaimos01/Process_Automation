import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_emails_auto(attachment_path, excel_attachment):
  '''Send automated emails via smtp server '''
  
    contacts = []
    cc = []
    mail_date = datetime.now().strftime("%B %d, %Y")
    subject = "Your Subject"  # Provide a meaningful subject
    mail_body = "<html><body>add an html structure or could also read from a txt file</body></html>"
    
    msg = MIMEMultipart('related')
    msg["Subject"] = f'{subject}: {mail_date}'
    msg["From"] = "your_preferred_email@example.com"
    msg["To"] = ", ".join(contacts)
    msg["Cc"] = ", ".join(cc)

    msg_body = MIMEText(mail_body, "html")
    msg.attach(msg_body)

    with open(os.path.join(attachment_path, excel_attachment), 'rb') as file:
        data = file.read()

    attach_file = MIMEBase('application', 'vnd.ms-excel')
    attach_file.set_payload(data)
    encoders.encode_base64(attach_file)
    attach_file.add_header('Content-Disposition', 'attachment', filename=excel_attachment)
    msg.attach(attach_file)

    server = smtplib.SMTP("your_smtp_server")
    server.sendmail(msg["From"], cc + contacts, msg.as_string())

if __name__ == "__main__":
    send_emails_auto("path/to/attachments", "example.xlsx")




  
  
  
  
