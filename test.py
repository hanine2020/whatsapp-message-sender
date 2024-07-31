import pywhatkit as kit

# Input the phone number (in the format: +[country_code][number])
phone_number = input("Enter the phone number (with country code, e.g., +1234567890): ")

# Input the message to send
message = input("Enter your message: ")

# Input the number of times to send the message
times = int(input("Enter the number of times you want to send the message: "))

# Current time
import datetime
now = datetime.datetime.now()

# Function to send message multiple times
def send_message_multiple_times(phone_number, message, times):
    for i in range(times):
        # Calculate the time to send the next message (1 minute apart)
        send_time = now + datetime.timedelta(minutes=i)
        kit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute + 1)

# Call the function
send_message_multiple_times(phone_number, message, times)


