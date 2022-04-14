try:
  	print("Hello,", name)
except NameError:
  print("Hello, stranger!")
else:
  print("What a beautiful name you have!")
finally:
  print("Hope to see you soon!")