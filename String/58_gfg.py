def duplicateCharacters(str):
    # convert characters to list 
    convertedList = list(str)
    # sort them
    convertedList.sort()

    i = 0
    # loop through the list
    while i < len(convertedList):
        count = 1
        # count the occurences of each character and check i doesnt go beyond the list range
        while (i < len(convertedList)-1 and (convertedList[i] == convertedList[i+1])):
            count += 1
            i += 1
        # print duplicate characters
        if (count > 1):
            print(f"count of {convertedList[i]} = {count}")
        i += 1

str = "Mississipi"
duplicateCharacters(str)
