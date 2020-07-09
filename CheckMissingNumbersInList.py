def checkMissing(table, long):
    allNumbersTable = list(range(1,long + 1))
    lenght = len(table) - 1
    stringTable = table[1:lenght].split(",")
    inputTable = []
    for item in stringTable:
        inputTable.append(int(item))
    inputTable.sort()
    outputTable = list(set(allNumbersTable) ^ set(inputTable))
