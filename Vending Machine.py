products = {
    'Chips': {'price': 1.50, 'stock': 5},
    'Mtn Dew': {'price': 1.00, 'stock': 5},
    'Coke': {'price': 2.50, 'stock': 5},
    'Dr Pepper': {'price': 2.00, 'stock': 0},
    'Snickers': {'price': 0.75, 'stock': 5}
}


print("Available Products:")
for product, details in products.items():
    print(f"{product}: ${details['price']} ({'In Stock' if details['stock'] > 0 else 'Out of Stock'})")


while True:
    choice = input("Please select a product: ").strip()
    if choice in products:
        if products[choice]['stock'] > 0:
            break
        else:
            print("Sorry, that product is out of stock.")
    else:
        print("Invalid selection. Try again.")

# Prices
price = products[choice]['price']
print(f"The price of {choice} is ${price:.2f}.")

# Pay
while True:
    try:
        payment = float(input(f"Insert ${price:.2f}: "))
        if payment >= price:
            break
        else:
            print("Insufficient amount. Please insert more money.")
    except ValueError:
        print("Invalid input. Please insert a valid amount.")

# Dispense
print(f"Dispensing {choice}. Enjoy!")

# Dispense change
change = payment - price
if change > 0:
    print(f"Dispensing change: ${change:.2f}")


products[choice]['stock'] -= 1


print("Thank you for your purchase!")


print("Goodbye!")
