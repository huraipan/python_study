import csv

data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자",85000,10,90000],
    ["NAVER",380000,5,400000]
]

file = open("./myvenv/Chapter10/mystock.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close