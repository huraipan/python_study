class PositiveNumberError(Exception):
  def __init__(self):
    super().__init__("+ not possible")

try:
  num = int(input("- type num>>>"))
  if num >= 0:
    raise PositiveNumberError
except PositiveNumberError as e:
  print("error", e)