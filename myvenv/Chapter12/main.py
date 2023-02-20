import os
import csv
from post import Post

file_path = "./myvenv/Chapter12/data.csv"

post_list = []

if os.path.exists(file_path):
    print("loading...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

print(post_list[0].get_title())