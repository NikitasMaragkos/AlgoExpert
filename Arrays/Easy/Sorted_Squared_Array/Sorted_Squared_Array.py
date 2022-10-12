def sortedSquaredArray(array):
    start = 0
    end = len(array) - 1
    squaredArray = [0 for _ in array]
    for idx in reversed(range(len(array))):

        leftValue = abs(array[start])
        rightValue = abs(array[end])

        if (leftValue < rightValue):
            squaredArray[idx] = rightValue * rightValue
            end -= 1
        else:
            squaredArray[idx] = leftValue * leftValue
            start += 1

    return squaredArray
