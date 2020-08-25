price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    price = price + price_of_item
    total_price = price
if total_price > 100:
    discount_price = total_price - (total_price * .10)
    print(f"Total price for {number_of_items} items is ${discount_price:,.2f}.")
else:
    print(f"Total price for {number_of_items} items is ${total_price}.")
