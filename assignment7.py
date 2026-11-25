import re #

text = "Contact us at abc@gmail.com or student123@yahoo.com for more information."

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' #describes the structure of email

emails = re.findall(pattern, text) #finfing all email

print("Email addresses found:")
for email in emails:
    print(email)
