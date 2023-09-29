from lib.order import Order
from twilio.rest import Client
from dotenv import load_dotenv
import os
from datetime import *

load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILIO_ACCOUNT_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

class OrderGenerator:

    def create_order(self, order_number, name):
        order = Order(order_number, name)
        return order
    
    def confirm_order(self, order):
        current_time = datetime.now()
        delivery_time = (current_time + timedelta(minutes=30)).strftime("%H:%M")
        message = client.messages.create(
        to=os.environ["MY_PHONE_NUMBER"], 
        from_=os.environ['TWILIO_PHONE_NUMBER'],
        body= f"Thank you for your order. Please expect delivery by {delivery_time}\n" + order.print_receipt())
        return message.sid