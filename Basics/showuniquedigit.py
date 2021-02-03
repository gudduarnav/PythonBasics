
def getdigits(num):
    listDigits = list()
    if num==0:
        listDigits.append(0)
    else:
        while num>0:
            listDigits.append(num%10)
            num = num//10
    listDigits.reverse()
    return listDigits

def uniqueDigit(num):
    digits = getdigits(num)
    maxDigit = max(digits)
    counter = 0
    for digit in digits:
        if digit==maxDigit:
            counter+=1
    return True if counter==1 else False

number = int(input("Enter a number:"))
print(uniqueDigit(number))