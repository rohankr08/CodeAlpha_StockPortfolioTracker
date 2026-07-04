stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200,
    "MSFT": 300
}

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print()

total_investment = 0
portfolio = []

while True:

    stock = input("Enter Stock Name (or type EXIT to finish): ").upper()

    if stock == "EXIT":
        break

    if stock in stock_prices:

        quantity = int(input("Enter Quantity: "))

        value = stock_prices[stock] * quantity

        total_investment += value

        portfolio.append([stock, quantity, value])

        print(f"Added Successfully! Value = ${value}\n")

    else:
        print("❌ Stock Not Found!\n")

print("\n" + "=" * 45)
print("          PORTFOLIO SUMMARY")
print("=" * 45)

for item in portfolio:
    print(f"{item[0]}   x {item[1]}   =   ${item[2]}")

print("---------------------------------------------")
print(f"Total Investment = ${total_investment}")

# Save to text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("===========================\n\n")

    for item in portfolio:
        file.write(f"{item[0]} x {item[1]} = ${item[2]}\n")

    file.write("\n---------------------------\n")
    file.write(f"Total Investment = ${total_investment}")

print("\n✅ Portfolio saved successfully in portfolio.txt")