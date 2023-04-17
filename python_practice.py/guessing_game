te a guessing game where the user guesses a number between 1 and 10 and the program tells them if it's the correct number '''
#generate random number
import random
random_digit = random.randrange(1,11)
i = 1
while (i != random_digit):
	i += 1
	print("the random number is : {}".format(random_digit))

#ask user to imput random number
	while True:
		try:
			number = int(input("guess a number between 1 and 10: "))

#compare random digit to user input
			if number == random_digit:
				print("You guessed it!{} is correct!".format(number))
			else:
				print("sorry, wrong number, try again")
			break
		except ValueError:
			print("you didn't enter a number")

		except:
			print("an unknown error occured"
