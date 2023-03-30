#have user enter their investment amount and expected yearly interest earned
money_invested = input("enter your investment amount: ")
money_invested = float(money_invested)
interest_rate  = input("enter your annual interest rate: ")
interest_rate = float(interest_rate) / 100
#investment increases by their original investment + current investment * annual interest rate
#print out earnings after a 10 yr period
for i in range(10):
  money_invested = money_invested + (money_invested * interest_rate)
print("your compounded interest is: {:.2f}".format(money_invested))