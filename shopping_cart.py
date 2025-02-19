import re
# Shopping cart
# Tasks:
# 1. Get item name from user
# 2. Get the quanity of the item from the user
# 3. Give the user a price for that item
# 4. Give a total price for the users purchase

# variables
item_name = ""
item_quantity = 0
item_price = 2.99
tax = 0.13
sub_total = 0
total_price = 0

# user inputs

# item_name input value
while True:
        item_name = input("Which item would you like to purchase?")
        if not re.match(r"^[A-Za-z\s]+$", item_name):
            print("Invalid input! Item name cannot contain numbers.")
            continue
        
        break

print(f"You selected: {item_name}")

# item_quantity input value
while True:
        item_quantity = input("Amount of the item you would like to purchase?")

        if not re.fullmatch(r"[1-9]\d*", item_quantity):  
            print("Invalid input! Please enter a positive whole number (no zero value, no decimals, letters, or leading zeros)")
            continue

        item_quantity = int(item_quantity)
        
        break
  
# calculate the total price for the user's item and quantity
sub_total = round(item_quantity * item_price, 0)
tax_total = round(sub_total * tax, 2)
total_price = round((sub_total + tax_total), 2)

# print total price to the user
print(f"Your item is: {item_name}")
print(f"Your quantity is: {item_quantity}", end="\n")
print(f"------------------------------------------------", end="\n")
print(f"Your item cost is: {item_price}")
print(f"Subtotal: {sub_total}")
print(f"Tax is: {tax_total}")
print(f"Total: {total_price}")
