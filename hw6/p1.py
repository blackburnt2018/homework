bowling = raw_input("if your would like to enter your bowling score by the entire game type 1, or if you would like to enter your play-by-play score type 2")

if(bowling == "1"):
	score = map(int, raw_input("enter your score from each frame separated by a comma").split(","))
	print(str(sum(score)))
	
