options = '' # declaring empty variable to be used in defining Options otherwwise it will keep looping 

# Outline available options
while options != "Q":
	print("[C] Convert from Celsius")
	print("[F] Convert from Fahrenheit")
	print("[M] Convert from Miles")
	print("[KM] Convert from Kilometres")
	print("[In] Convert from Inches")
	print("[CM] Convert from Centimetres")
	print("[Q] Quit")

	print() # Space out

	# Ask user for options
	options = input ("Enter the options [C, F, M, KM, In, CM, Q]? ")
	print()
	if options == "C":
		# Converting from Celsius to Fahrenheit
		celsius = float(input("Celsius temperature: "))
		temp = (celsius * 1.8) + 32
		print ('Fahrenheit: ' +str(temp))
		print()
	elif options == "F":
		# Converting from Fahrenheit to Celsius
		fahrenheit = float(input("Fahrenheit temperature: "))
		temp = (fahrenheit - 32) * 0.55
		print('Celsius: ' + str(temp))
		print()
	elif options == "M":
		# Converting Miles to Kilometres
		miles = float(input("Miles: "))
		kilometres = miles * 1.609344
		print("Kilometres: " + str(kilometres))
		print()
	elif options == "KM":
		# Converting Kilometres to Miles
		kilometres = float(input("Kilometres: "))
		miles = (kilometres * 0.621371)
		print("Miles: " + str(miles))
		print()
	elif options == "In":
		# Converting Inches to Centimetres
		inches = float(input("Inches: "))
		centimetres = inches * 2.54
		print("Centimetres: " + str(centimetres))
		print()
	elif options == "CM":
		# Converting Centimetres to Inches
		centimetres = float(input("Centimetres: "))
		inches = centimetres / 2.54
		print("Inches: " + str(inches))
		print()
	else:
		print("Invalid input!!!")
		print()
