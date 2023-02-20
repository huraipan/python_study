won = input("please write won>>>")
dollar = input("please write >>>")


try:
    print(int(won) / int(dollar))
except ValueError as e:
    print("String error", e)
except ZeroDivisionError as e:
    print("0is not possiavle", e)
else:
    print("not error")
finally:
    print("always")
