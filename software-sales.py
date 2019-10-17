# Program 3-12 Software Sales
# Shaun Hayworth
# CIS 2
# 10-16-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/3-12-Softare-Sales

# Calculates the total price of a software package after a discount based on the number of packages purchased.

# Intitialize the PRICE_CONSTANT variable and set it to 99.0
# Modify this if the price changes
PRICE_CONSTANT = 99.0

# Initialize the discount_multiplier variable and set it to 0.0. This will be used to determine the total discount
discount_multiplier = 0.0

# Prompt user for the number of packages purchased and store the result in packages_purchased.
packages_purchased = int(input('Enter the number of packages purchased: '))

# Calculate the base price of the purchase by multiplying PRICE_CONSTANT by packages_purchased.
base_price = PRICE_CONSTANT * packages_purchased

# Determine the discount_multiplier based on packages_purchased.
if packages_purchased >=10 and packages_purchased <= 19:
  discount_multiplier = 0.1
elif packages_purchased >=20 and packages_purchased <= 49:
  discount_multiplier = 0.2
elif packages_purchased >=50 and packages_purchased <= 99:
  discount_multiplier = 0.3
elif packages_purchased >=100:
  discount_multiplier = 0.4
else:
  discount_multiplier = 0.0

# Calculate discount_amount by multiplying base_price by discount_multiplier
discount_amount = base_price * discount_multiplier

# Calculate total_price by subtracting discount_amount from base_price.
total_price = base_price - discount_amount

# Display the amount discounted and the total price onscreen.
print(f'Discount Amount: ${discount_amount:.2f}')
print(f'Total Amount: ${total_price:.2f}')
