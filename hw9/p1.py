import random

rollresult1 = 0
rollresult2 = 0
score1 = 0
score2 = 0
rollrange = [1,6]
ledger = []


def roll(beginning,end):
	return random.randint(beginning,end)

def determineWinnerRound(rollresult1,rollresult2):
	if(rollresult1 > rollresult2):
		return "player1 wins round 1"
	elif(rollresult2 > rollresult1):
		return "player2 wins round 1"
	else:
		return "tie"

def determineWinnerGame(score1,score2):
	if(score1 > 1):
		return "player1"
	elif(score2 > 1):
		return "player2"
	else:
		return "nobody"


gamerunning = True

while(gamerunning):
	if(rollresult1 > rollresult2):
		return score1 += 1
	elif(rollresult2 > rollresult1):
		return score2 += 1
	elif(rollresult1 = rollresult2):
		
