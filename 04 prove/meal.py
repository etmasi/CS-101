child_meal =input (("Enter the price of the child's meal:"))
adult_meal = input ( ("Enter the price of the adult's meal:"))
meal_price = (float(child_meal) + float(adult_meal))


childen_number = input("Enter the number of children:")
adults_number = input("Enter the number of adults:")
people_number = (int(childen_number) + int(adults_number))
sales_tax_rate = input("Enter sales tax:")



subtotal = childen_number * child_meal + adults_number * adult_meal

sales_tax = print(subtotal * sales_tax_rate / 100)

total_price = print(subtotal + sales_tax)

payment = input( "How much did you pay?")

change = input(payment - total_price))