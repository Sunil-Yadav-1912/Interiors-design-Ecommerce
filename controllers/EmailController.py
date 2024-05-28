import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


def send_order_email(order_details):
    # Email configurations

    smtp_server = config.SMTP_SERVER
    smtp_port = config.SMTP_PORT
    smtp_username = config.SMTP_USERNAME
    smtp_password = config.SMTP_PASSWORD
    sender_email = config.SENDER_EMAIL
    recipient_email = config.RECIPIENT_EMAIL

    # Construct the message

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Order Details'

    # Construct the email body
    email_body = f"Order Details:\n\n"
    email_body += f"Total Amount: {order_details['totalAmount']}\n"
    email_body += f"Shipping: {order_details['shipping']}\n"
    email_body += f"Discount Code: {order_details['discountCode']}\n\n"
    email_body += "Items:\n"
    for item in order_details['items']:
        email_body += f"Item ID: {item['itemId']}, Quantity: {item['quantity']}, Price: {item['price']}, Name: {item['name']}\n"
    email_body += "\n"
    msg.attach(MIMEText(email_body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the connection
    server.quit()

    return 1

def send_subscription_email(name, email):
    # Email configurations
    smtp_server = config.SMTP_SERVER
    smtp_port = config.SMTP_PORT
    smtp_username = config.SMTP_USERNAME
    smtp_password = config.SMTP_PASSWORD
    sender_email = config.SENDER_EMAIL
    recipient_email = config.RECIPIENT_EMAIL

    # Construct the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'New Subscription'

    # Construct the email body
    email_body = f"New subscription details:\n\n"
    email_body += f"Name: {name}\n"
    email_body += f"Email: {email}\n"
    msg.attach(MIMEText(email_body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the connection
    server.quit()