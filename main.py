while True:
  try:
    name, surname = input().split()
  except ValueError:
    print("You need to enter exactly 2 words. Try again!")
  else:
    print(f"Welcome to our party, {name} {surname}")
    break