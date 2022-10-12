def twoNumberSum(array, targetSum):
    visitedNumbers = {}
    for fisrtNumber in array:
        secondNumber = targetSum - fisrtNumber
        if secondNumber in visitedNumbers:
            return [fisrtNumber, secondNumber]
        visitedNumbers[fisrtNumber] = True
    return []
