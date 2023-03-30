#Enter calculation eg, 5 * 6
#output: 5 * 6 = 30
#Store the user input of 2 numbers and their operatior
num1, operator, num2, = input("enter calculation (seperate numbers and operators using spaces): ").split()
#Convert strings into inegers
num1 = int(num1)
num2 = int(num2)
#if +, provide addition input, same for -,*,/...
#solution 1
'''sum = num1 + num2
difference = num1 - num2
mult = num1 * num2
division = num1 / num2
if operator == "+":
  print("{} + {} = {}".format(num1, num2, sum))
if operator == "-":
  print("{} - {} = {}".format(num1, num2, difference))
if operator == "*":
  print("{} * {} = {}".format(num1, num2, mult))
if operator == "/":
  print("{} / {} = {}".format(num1, num2, division))'''
#solution 2
'''if operator == "+":
  print("{} + {} = {}".format(num1, num2, num1+num2))
if operator == "-":
  print("{} - {} = {}".format(num1, num2, num1-num2))
if operator == "*":
  print("{} * {} = {}".format(num1, num2, num1*num2))
if operator == "/":
  print("{} / {} = {}".format(num1, num2, num1/num2))'''
#solution 3
if operator == "+":
  print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
  print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
  print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
  print("{} / {} = {}".format(num1, num2, num1/num2))
else:
  print("error, please use the +, -, *, / operators ")