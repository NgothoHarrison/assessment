# import africastalking
# from django.conf import settings
# import re

# # Initialize the Africa's Talking client
# africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
# sms = africastalking.SMS

# def send_sms(phone_number, message):
#     # Ensure the phone number is valid
#     phone_regex = re.compile(r'^\+?1?\d{9,15}$')
#     if not phone_regex.match(phone_number):
#         raise ValueError(f"Invalid phone number format: {phone_number}")
    
#     try:
#         response = sms.send(message, [phone_number], settings.AFRICASTALKING_SENDER_ID)
#         print(response)
#     except Exception as e:
#         print(f"Failed to send SMS: {str(e)}")

import africastalking
from decouple import config  # To load .env variables

# Initialize Africa's Talking SDK
africastalking.initialize(
    username=config('AFRICASTALKING_USERNAME'),
    api_key=config('AFRICASTALKING_API_KEY')
)

# Get SMS service
sms = africastalking.SMS 

def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        # Check if the response indicates success
        if response['status'] == 'success':
            print(f"SMS sent successfully to {phone_number}: {response}")
            return response
        else:
            print(f"Failed to send SMS: {response}")
            return None
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None


