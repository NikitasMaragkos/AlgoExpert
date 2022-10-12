def isValidSubsequence(array, sequence):
	if len(array)  < len(sequence):
		return False
    firstIndex = 0
	for aNumber in sequence:
		if len(array) - 1 < firstIndex:
			return False
		findIt = False
		for i in range(firstIndex, len(array)):
			if array[i] == aNumber:
				findIt = True
				firstIndex = i + 1
				break
		if not findIt:
			return False
	return True
