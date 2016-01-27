balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#previousBalance = balance



numMonths = 12
monthCounter = 0
totalPaid = 0
for i in range(0,12):
	monthlyInterestRate = annualInterestRate / 12.0

	minimumMonthlyPayment = round((monthlyPaymentRate * balance),2)

	monthlyUnpaidBalance = round(balance - minimumMonthlyPayment,2)
    #previousBalance -= minimumMonthlyPayment

	balance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),2)
    

	monthCounter += 1
    print "Month %r: " % monthCounter
    print "\rMinimum Monthly Payment: %r" % minimumMonthlyPayment
    print "\rRemaining Balance: %r" % balance
    totalPaid += minimumMonthlyPayment

print "\rTotal Paid: %r" % round(totalPaid,2)
print "\rRemaining Balance: %r" % balance
