# Task--1
"""
import re

#text = """
#Contact numbers are 9876543210 and 8123456789.
#The price is 999 and another number is 654321.
#You can also contact 9123456780.
"""

pattern = r'\b[789]\d{9}\b'

phone_numbers = re.findall(pattern, text)

print("Valid Indian phone numbers:")
print(phone_numbers)"""

# Task--2

"""import re

def check_date(date_string):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    if re.search(pattern, date_string):
        return True
    else:
        return False


print(check_date("Today is 25/06/2024"))
print(check_date("Meeting is on 5/6/2024"))
print(check_date("Date: 25-06-2024"))"""

# Task--3
import re

text = """
Great food and fast delivery!
Contact restaurant at food@example.com.
For complaints email support@zomato.com.
You can also write to customer.help@gmail.com.
"""

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses:")
print(emails)

# Task--4

import re

phone = "9876543210"

masked_phone = re.sub(r'\d(?=\d{4})', '*', phone)

print("Original phone:", phone)
print("Masked phone:", masked_phone)

# Task--5

import re

order_ids = [
    "OD123456789012345000",
    "OD987654321012345678",
    "AB123456789012345000",
    "OD12345"
]

pattern = r'\bOD\d{18}\b'

for order_id in order_ids:
    if re.search(pattern, order_id):
        print(order_id, "→ Valid order ID")
    else:
        print(order_id, "→ Invalid order ID")