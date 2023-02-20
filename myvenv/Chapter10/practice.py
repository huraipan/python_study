import csv

def show_profit(data):
    name = data[0]
    purchase_price = int(data[1])
    amount = int(data[2])
    target_price = int(data[3])

    profit = (target_price - purchase_price) * amount
    profit_ratio = (target_price/purchase_price - 1) * 100

    print(f"{name} {profit}, {profit_ratio : .2f}%")

file = open("./myvenv/Chapter10/mystock.csv", "r", encoding="utf-8-sig")

reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)

file.close()
