#ask user to input 2 values and store them in a variable
num1, num2 = input('enter 2 numbers: ').split()
#convert strings into integers
num1 = int(num1)
num2 = int(num2)
#add the values entered and store in sum variable
sum = num1 + num2
#subtract and store in difference
difference = num1 - num2
#multiply and store in product
product = num1 * num2
#divide and store in quotient
quotient = num1 / num2
#find remainder and store in modulous
modulous = num1 % num2
#print result
#print('num1 + num2 = ', sum)
print("{} + {} = {}".format (num1, num2, sum))
#print('num1 - num2 = ', difference)
print("{} - {} = {}".format (num1, num2, difference))
#print('num1 x num2 = ', product)
print("{} * {} = {}".format (num1, num2, product))
#print('num1 / num2 = ', quotient)
print("{} / {} = {}".format (num1, num2, quotient))
#print('num1 % num2 = ', modulous)
print("{} % {} = {}".format (num1, num2, modulous))