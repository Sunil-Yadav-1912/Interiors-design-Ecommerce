from models.email_model import send_email

def send_order_email(order_details, user_details, total_amount):
    email_body = "Order Details:\n\n"
    email_body += f"Customer Name: {user_details.get('first_name', 'N/A')} {user_details.get('last_name', 'N/A')}\n"
    email_body += f"Email: {user_details.get('email', 'N/A')}\n"
    email_body += f"Phone: {user_details.get('mobile', 'N/A')}\n"
    email_body += f"Address: {user_details.get('address', 'N/A')}, {user_details.get('city', 'N/A')}, {user_details.get('state', 'N/A')}, {user_details.get('country', 'N/A')}, {user_details.get('postal_code', 'N/A')}\n\n"
    email_body += f"Total Amount: {total_amount}\n"
    email_body += "Items:\n"
    for item in order_details:
        email_body += f"Item ID: {item.get('itemId', 'N/A')}, Name: {item.get('name', 'N/A')}, Quantity: {item.get('quantity', 'N/A')}, Price: ${item.get('price', 0.00):.2f}, Discount Coupon: ${item.get('discountCode', 0.00)}\n"
    email_body += "\n"
    send_email('Order Details', email_body)
    return 1

def send_subscription_email(name, email):
    email_body = f"New subscription details:\n\n"
    email_body += f"Name: {name}\n"
    email_body += f"Email: {email}\n"
    send_email('New Subscription', email_body)

def send_contact_us_email(data):
    email_body = f"New contact us message:\n\n"
    email_body += f"First name: {data.get('first_name', 'N/A')}  Last name : {data.get('last_name', 'N/A')}\n\n"
    email_body += f"Email: {data.get('email', 'N/A')}\n\n"
    email_body += f"Message: {data.get('message', 'N/A')}\n"
    send_email('Contact us message', email_body)
