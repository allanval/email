import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def generate_email(sender_email, receiver_email, subject, body, attachments=[]):
    
    msg = MIMEMultipart()

    
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    
    msg.attach(MIMEText(body, 'html'))

    
    for attachment_path in attachments:
        attach_file(msg, attachment_path)

    return msg

def attach_file(msg, file_path):
    
    with open(file_path, 'rb') as attachment:
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

        
        encoders.encode_base64(part)

        
        part.add_header('Content-Disposition', f'attachment; filename= {file_path}')

        
        msg.attach(part)

def send_email(sender_email, sender_password, receiver_email, subject, body, attachments=[]):
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    
    email_message = generate_email(sender_email, receiver_email, subject, body, attachments)

    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    
    server.login(sender_email, sender_password)

    
    server.sendmail(sender_email, receiver_email, email_message.as_string())

    
    server.quit()


sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'recipient_email@example.com'
email_subject = 'Real-world Email Example'
email_body = '<p>This is a real-world example of sending HTML email with attachments using Python.</p>'


attachment_paths = ['file1.txt', 'image.jpg']


send_email(sender_email, sender_password, receiver_email, email_subject, email_body, attachment_paths)
