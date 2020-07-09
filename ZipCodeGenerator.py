def zipCodeGenerator (zip1, zip2):
    zip1Table = zip1.split('-')
    zip2Table = zip2.split("-")
    zipCodesTableFirst = []
    zipCodesTableSecond = []
    finalTable = []
    numberOne = int(zip1Table[0]) + 1
    numberTwo = int(zip2Table[0])

    if (numberTwo < numberOne):
        temp = numberOne
        numberOne = numberTwo
        numberTwo = temp

    while numberOne < numberTwo:
        zipCodesTableFirst.append(numberOne)
        numberOne += 1

    numberOne = int(zip1Table[1])
    numberTwo = int(zip2Table[1])

    if (numberTwo < numberOne):
        temp = numberOne
        numberOne = numberTwo
        numberTwo = temp

    while numberOne < numberTwo:
        if(numberOne == 999):
            numberOne = 0
        numberOne += 1
        zipCodesTableSecond.append(numberOne)
    zipCodesTableSecond.pop()

    for item in zipCodesTableFirst:
        for item2 in zipCodesTableSecond:
            if(item2 < 10):
                finalTable.append(str(item) + "-" + "00" + str(item2))
            elif(item2 < 100):
                finalTable.append(str(item) + "-" + "0" + str(item2))
            else:
                finalTable.append(str(item) + "-" + str(item2))
