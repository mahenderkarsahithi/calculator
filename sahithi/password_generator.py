import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*# "

upper, lower, numbers, symbols = True, True, True, True
all =""

if upper:
     all += uppercase_letters
if lower:
     all += lowercase_letters
if numbers:
     all += digits
if symbols:
     all += symbols

length = 20
amount = 10

for x in range(amount):
     password = "".join(random.sample(all, length))
     print(password)