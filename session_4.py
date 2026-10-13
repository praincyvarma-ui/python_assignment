# Task . 1 upper() and lower()

"""product_name = "redmi note 12 pro"

print("uppercase:",product_name.upper())
print("lowercase:",product_name.lower())"""

# Task .2 strip()  replace() function.

"""def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name 

print(clean_brand_name( " one-plus "))"""

# Task . 3 string silicing
"""
products = " apple iphone 14 pro max "

words = products.split()

brand = words[0]
model = " ".join(words[1:])

print("brand:", brand)
print("model:", model)"""

# Task . 4 function +formatting string

"""def format_product_display(name,price):
    return f"{name} - {price}"

print(format_product_display("Boat Earbuds", 1299))"""

# Task . 5 list cleaning + 3 string method

product_names = ['mi-Band 5','SAMSUNG-Galaxy','realme-Book']
clean_names = []

for name in product_names:
     name = name.strip()
     name = name.replace("-"," " )
     name = name.title()

     clean_names.append(name)

print(clean_names)