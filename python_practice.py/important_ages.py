#provide different outputs based on age
'''
1-18 -> important
21, 50, >60 -> Important
all others -> not important'''
#receive age and store in age variable
age = eval(input("enter your age: "))
#logical operators
'''
and: if both conditions are true, return True
or: if eitherconditions are true return True
not: convert a true condition into false and vice versa'''
#if age is both >= 1 and <= 18, important
if (age >= 1) and (age <= 18):
  print("important")
#if age is either 21 or 50, important
elif (age == 21) or (age == 50):
  print("important")
#we check if age is less than 65 then convert true to false and vice versa
elif not(age < 65):
  print("important")
#Else, not important
else:
  print("not important")