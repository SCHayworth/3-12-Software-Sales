# 3-12 Software Sales
## Scope
A software company sells a package that retails for $99. Quantity discounts are given according to the following table:

    Quantity      Discount
    10-19         10%
    20-49         20%
    50-99         30%
    100 or more   40%

Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.

### Sample Run
    Enter the number of packages purchased: 55
    Discount Amount: $1633.50
    Total Amount: $31811.50

## Pseudocode
    Set the number of packages to 0
    Set the retail price constant to 99.0
    Prompt user for the number of packages
    Calculate the base price before discount
      base price = retail price * number of packages
    Calculate the discount multiplier
      IF number of packages >= 10 AND <=19
        THEN discount multiplier = 0.1
      IF number of packages >=20 AND <= 49
        THEN discount multiplier = 0.2
      IF number of packages >=50 AND <=99
        THEN discount multiplier = 0.3
      IF number of packages >= 100
        THEN discount multiplier = 0.4
      ELSE discount multiplier = 0
    Calculate the discount amount
      discount amount = base price * discount multiplier


