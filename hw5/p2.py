currentNumber = float(input("give me an integer: "))
if(currentNumber % 2.0) == 0.0:
	evennumber = currentNumber * 3 + 1
	print(evennumber)
else:
	oddnumber = currentNumber // 2
	print(oddnumber)
