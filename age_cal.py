
from datetime import datetime
print("Hello there...")
print ("We are calculating your age")
y = input("Please enter your name: ")
x = int(input("Enter your Bday year: "))
current_year = datetime.now().year

print(" ")
print(" ")
print("Plese wait...")
print("Calculating your age.....")
print("NAME: ",y)
print("BDay year: ",x)
sum = current_year - x
print("Your present age is:", sum)