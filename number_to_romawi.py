# number to Roman values
import math

A = int(input('Insert Number (max val = 100 million): '))

def integerToRoman(A):
    # create a roman numeral dictionary
	romansDict = \
		{
			1: "I",
			5: "V",
			10: "X",
			50: "L",
			100: "C",
			500: "D",
			1000: "M",
			5000: "V`",
			10000: "X`",
            50000: "L`",
            100000: "C`",
            500000: "D`",
            1000000: "M`",
            # The roman numerals below are just my example
            # if the number entered by the user reaches 100 million
            5000000: "V``",
            10000000: "X``",
            50000000: "D``",
            100000000: "C``"
		}
    # 
	div = 1
	while A >= div:
		div *= 10

	div /= 10

	res = ""

	while A:

		# main significant digit extracted
		# into lastNum
		lastNum = int(A / div)

		if lastNum <= 3:
			res += (romansDict[div] * lastNum)
		elif lastNum == 4:
			res += (romansDict[div] + romansDict[div * 5])
		elif 5 <= lastNum <= 8:
			res += (romansDict[div * 5] + (romansDict[div] * (lastNum - 5)))
		elif lastNum == 9:
			res += (romansDict[div] + romansDict[div * 10])

		A = math.floor(A % div)
		div /= 10
		
	return res

# Driver code
print("Roman value for the integer is:" + str(integerToRoman(A)))
