#program determines which grade people should be in
#complete with 10 or less lines
#person should input their age(store in age variable)
age = eval(input("what is your age? "))
if age < 5:
 print("sorry, you need to be above 5 years old to go to school")
#if age is 5, print go to kindergarten
elif age == 5:
 print("go to kindergarten") 
#age 6-17 print go to grade 1-12
elif (age > 5) and (age <= 17):
  #create a grade variable
  grade = age - 5
  print("go to {} grade".format(grade))
#if age is greater than 17 print go to college
else:
  print("go to college")