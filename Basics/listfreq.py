
def frequency(numList):
    counterList = dict()
    for n in numList:
        if n in counterList.keys():
            counterList[n] += 1
        else:
            counterList[n] = 1

    maxKey = None
    maxVal = None
    for (key, val) in counterList.items():
        if maxKey is None:
            maxKey = key
            maxVal = val
        elif val > maxVal:
            maxKey = key
            maxVal = val

    return (maxKey, counterList)

l = input("Enter elements separated by space:").strip().split(",")
print("List is", l)

tup = frequency(l)
print(tup)
