# credit_calculator
Calculates values for annuities and differentiated payments using CLI.

To calculate the values via command line, you must specify the following:
- the type of payment ("diff" for differentiated or "annuity" for annuity)
- the known parameters

If the command line argument is entered correctly, the program will calculate the unknown variable; otherwise, the program will generate an error message.

For differentiated payments, the principal amount, number of periods (in months), and annual interest rate (as a percentage) must be inputted. Each parameter is preceded by two dashes, "--", followed by an equals sign, ending with the value for the parameter.

An example of a correct command line argument for a differentiated payment is:

	python credit_calc.py --type=diff --principal=500000 --periods=8 --interest=7.8

Which would print out the payment for each month, as well as the "overpayment" (the total interest paid):

	Month 1: paid out 65750
	Month 2: paid out 65344
	Month 3: paid out 64938
	Month 4: paid out 64532
	Month 5: paid out 64125
	Month 6: paid out 63719
	Month 7: paid out 63313
	Month 8: paid out 62907

	Overpayment = 14628

For annuities, the annual interest rate (as a percentage) must always be specified. Two of the following must also be specified: the principal amount, number of periods (in months), and/or the monthly payment. Any combination of two of those three parameters must be inputted in order to output the unknown parameter. For example, if the number of periods and the monthly payment are specified, the program will calculate the principal. The overpayment is also always calculated.

An example of a correct command line argument for an annuity payment is:

	python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6

Which would print out:

	Your credit principal = 800018!
	Overpayment = 246622

