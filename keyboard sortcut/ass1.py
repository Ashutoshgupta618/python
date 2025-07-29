import os
import time
import smtplib
import pywhatkit 
import platform
from email.message import EmailMessage


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

print("Choose an option:")
print("1: Create folder on Desktop")
print("2: Create file in folder")
print("3: Send WhatsApp message")
print("4: Send email to hr@regexsoftware.com")
print("5: Shutdown PC and sleep")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    folder_path = os.path.join(get_desktop_path(), "ashutosh")
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created at: {folder_path}")

elif choice == "2":
    folder_path = os.path.join(get_desktop_path(), "ashutosh")
    os.makedirs(folder_path, exist_ok=True) 
    file_path = os.path.join(folder_path, "myfile.txt")
    with open(file_path, "w") as file:
        file.write("Hello! This is a test file created by ashutosh.")
    print(f"File created at: {file_path}")

elif choice == "3":
    try:
       
        phone_number = "7877088966"  
        message = "Hey! This is a test message sent using Python."
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M")) + 1  
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        print("WhatsApp message scheduled successfully.")
    except Exception as e:
        print("Failed to send WhatsApp message:", e)

elif choice == "4":
    try:
        # Configure your email credentials
        sender_email = "ag0824230@gmail.com"
        sender_password = "nahi batau"
        receiver_email = "hr@regexsoftware.com"

        msg = EmailMessage()
        msg.set_content("Dear HR,\n\nThis is a test email from Python script.")
        msg["Subject"] = "Test Email"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

elif choice == "5":
    print("Shutting down the PC in 10 seconds...")
    time.sleep(10)
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown now")
    else:
        print("Unsupported OS")

else:
    print("Invalid input.")