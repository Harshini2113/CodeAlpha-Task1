stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0
details = []

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

n = int(input("Enter number of different stocks you want to buy: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        investment = stocks[name] * quantity
        total_investment += investment
        details.append(f"{name} - Quantity: {quantity}, Value: ${investment}")
    else:
        print("Stock not available")

print("\nTotal Investment Value: $", total_investment)

# Saving result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    for item in details:
        file.write(item + "\n")
    file.write("\nTotal Investment Value: $" + str(total_investment))

print("Portfolio saved successfully in 'portfolio.txt'")
