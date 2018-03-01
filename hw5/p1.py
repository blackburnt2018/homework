temperature = raw_input("what is the reading on a thermometer")
answer = raw_input("do you feel warm")

if(temperature >= "96" and answer == "no"):
	print("try dessing up for the winter to keep your temperature up")
	if(temperature >= "96" and answer == "yes"):
		print("hmph, you must be cold blooded")
elif(temperature <= "99" and answer == "yes"):
	print("you may be running a fever")
	if(temperature <= "99" and answer == "no"):
		print("you must be warm blooded")
elif(temperature == "98.6" and answer == "no"):
	print("congratulations, you are normal and healthy")
