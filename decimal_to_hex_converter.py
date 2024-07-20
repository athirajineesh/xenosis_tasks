dectohex="0123456789ABCDEF"
def dectohexadecimal(decimal):
	hexadecimal = ''   # initialising to zero
	while(decimal > 0): # check whether greater than zero
		remainder = decimal % 16 #divide by 16 and keep the remainder
		hexadecimal = dectohex[remainder] + hexadecimal #set to the hex value of remainder
		decimal = decimal // 16 # set decimal = the number we got other than the remainder, which we want to divide by 16 further until we get the 0 as quotient
# repeat the process and append each hex to the previous one
	return hexadecimal


decimal_number = int(input("Input: "))
hexadecimal = dectohexadecimal(decimal_number)
print("Output: " + hexadecimal)

