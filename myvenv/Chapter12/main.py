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

def write_post():
    """write function"""
    print("\n\n- write -")
    title = input("please write title\n >>>")
    content = input("please write content\n >>>")

    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# good good")


def list_post():
    """list function"""
    print("\n\n- list -")
    id_list = []
    for post in post_list:
        print("num :", post.get_id())
        print("title :", post.get_title())
        print("count :", post.get_view_count())
        print("")
        id_list.append(post.get_id())
    while True:
        print("Q) please select num (if you want to go back please type -1)")
        try:
                id = int(input(">>>"))
                if id in id_list:
                    detail_post(id)
                    break
                elif id == -1:
                    break
                else:
                    print("not exist number")
        except ValueError:
            print("please input num")

def detail_post(id):
    print("\n\n- view text -")

    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print("num :", post.get_id())      
            print("title :", post.get_title())    
            print("content :", post.get_content())    
            print("view_count :", post.get_view_count())     
            target_post = post

    while True:
        print("Q) modify: 1  delete: 2 (go back menu: -1)")     
        try:
            choice = int(input(">>>"))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("please input again")
        except ValueError:
            print("please input num")

def update_post(target_post):
    """modify function"""
    print("\n\n- update text -")
    title = input("write title \n>>>")
    content = input("write content \n>>>")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("update is done")


def delete_post(target_post):
    post_list.remove(target_post)
    print("delete is done")


def save():
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("save is done")
    print("exit")

while True:
    print("\n\n- FASTCAMPUST BLOG -")
    print("- select menu -")
    print("1. write")
    print("2. list")
    print("3. exit")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("input num")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            save()
            break