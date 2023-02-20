

try:
  num = int(input("- type num>>>"))
  if num >= 0:
    raise ValueError("+ is not")
except ValueError as e:
  print("error", e)
