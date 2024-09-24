
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


