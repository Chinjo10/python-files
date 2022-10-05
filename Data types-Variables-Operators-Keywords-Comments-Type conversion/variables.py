# to exlpain the variables concept

items_count = 100
customer_name = 'vamsi'
is_bill_paid = False
unit_price = 15.05

#print(id(items_count ))

print('items_count: ', items_count, 'type of items_count: ',
      type(items_count), 'memory loction: ', id(items_count))
print('customer_name: ', customer_name, 'type of customer_name: ',
      type(customer_name), 'memory loction: ', id(customer_name))
print('is_bill_paid: ', is_bill_paid, 'type of is_bill_paid: ',
      type(is_bill_paid), 'memory loction: ', id(is_bill_paid))
print('unit_price: ', unit_price, 'type of price: ', type(
    unit_price), 'memory loction: ', id(unit_price))

total = items_count * unit_price

discount = 50

total_after_discount = total - discount


print('toal bill to be paid: ', total - discount)

print("Total before discount:",total )
print("Total after discount:",total_after_discount)


print("items_count:", items_count)
