child_meal =input (("Enter the price of the child's meal:"))
adult_meal = input ( ("Enter the price of the adult's meal:"))


children_number = input("Enter the number of children:")
adults_number = input("Enter the number of adults:")
print (int(children_number) + int(adults_number))
sales_tax_rate = input("Enter sales tax:")



# subtotal = int(( children_number * child_meal) + int (adults_number * adult_meal))
subtotal = (int(children_number) * int(child_meal)) + (int(adults_number) * int(adult_meal))

sales_tax = print(subtotal * int(sales_tax_rate) / 100)
total_price = print(subtotal + int(sales_tax_rate))

payment = input( "How much did you pay?")

print(subtotal)
print(sales_tax_rate)
print(payment)
print(total_price)

change = int(payment) -  int(total_price)