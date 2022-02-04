from LessonOne import lesson1

# Тест 1
# Входные данные: 2, 5, 5
# Ожидаемый результат: 12

# Тест 2
# Входные данные: 11, 23, 8
# Ожидаемый результат: 42

# Тест 3
# Входные данные: 0, 0, 0
# Ожидаемый результат: 0

testInputs = [
    [2, 5, 5], 
    [11, 23, 8], 
    [0, 0, 0]
]
testExpectedResults = [12, 42, 0]
testMsges = []

def test():
    i = 0
    isTestPassed = True
    for testInput in testInputs:
        expectedTestResult = testExpectedResults[i]
        testResult = lesson1(testInput[0], testInput[1], testInput[2])
        if (testResult == expectedTestResult):
            testMsges.append(formatResultMessage(i + 1, testResult, expectedTestResult, True))
            isTestPassed &= True
        else:
            testMsges.append(formatResultMessage(i + 1, testResult, expectedTestResult, False))
            isTestPassed &= False
        i += 1
    if isTestPassed: 
        print("Все тесты прошли успешно!")
    else: 
        print("Не все тесты прошли успешно:")
        for msg in testMsges:
            print(msg)


def formatResultMessage(testNum, result, expectedResult, passed):
    msg = ""
    msg += "Тест №" + str(testNum) + (" прошёл успешно." if passed else " провален.") + " "
    msg += "Твой результат: " + str(result) + ", ожидаемый результат: " + str(expectedResult)
    return msg

test()