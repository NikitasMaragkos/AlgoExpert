def tournamentWinner(competitions, results):
    scoreBoard = {}
	for match,result in zip(competitions,results):
		if result:
			scoreBoard[match[0]] = scoreBoard[match[0]] + 3 if match[0] in scoreBoard.keys() else 3
		else:
			scoreBoard[match[1]] = scoreBoard[match[1]] + 3 if match[1] in scoreBoard.keys() else 3
    return max(scoreBoard, key = scoreBoard.get)
