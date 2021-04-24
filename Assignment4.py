#Enter the price of the House you wish to Buy
print("Enter the house price")
price = float(input())
#Enter the credit score
print("Enter the credit score")
CreditScore = int(input())
#Enter the first name
print("Enter the first name")
first_name = input()
#Enter the last name
print("Enter the last name")
last_name = input()
fullname = first_name + " " + last_name
#Enter the email
print("Enter the email address")
email = input()
#Enter the phone number
print("Enter the phone number")
phone = input()
#Enter the mailing
print("Enter the mailing address")
address = input()
#Enter the mailing
print("Enter the City")
city = input()
#Enter the mailing
print("Enter the zip code")
zipcode = input()

print()

#Qualify for loans with the best interest rates
if CreditScore >= 780 and 850:
	print ("Excellent Credit")
	print("Zero Down Payment")
	downPayment = 0.0 * price
	print("Downpayment: " + str(downPayment))
#Usually qualify for loans with the best interest rates
elif CreditScore >= 740 and 779:
	print("Very Good")
	downPayment = 0.2 * price
	print("Downpayment: " + str(downPayment))
#May face slightly higher loan Interest rates
elif CreditScore >= 720 and 739:
	print("Above Average")
	downPayment = 0.3 * price
	print("Downpayment: " + str(downPayment))
#May qualify for most loans of higher interest rates
elif CreditScore >= 680 and 719:
	print("Average")
	downPayment = 0.6 * price
	print("Downpayment: " + str(downPayment))
#May qualify for most loans at significant higher Interest rates
elif CreditScore >= 620 and 679:
	print("Below Average")
	downPayment = 0.18 * price
	print("Downpayment: " + str(downPayment))
#Usually has some credit issues; will probably not qualify for most loans
elif CreditScore >= 580 and 619:
	print("Poor Credit Score")
	downPayment = 0.20 * price
	print("Downpayment: " + str(downPayment))
#Facing extreme credit issue
elif CreditScore < 520:
	print("Poor Credit Score")
	downPayment = 0.25 * price
	print("Downpayment: " + str(downPayment))
else:
	print("invalid output")


print("Full name is: " + fullname)
print("Physical address: " + address)
print("City: " + city)
print("Zipcode: " + zipcode)