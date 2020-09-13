def checkPalindrome(st):
    countOdd = 0
    countArr = [0]*26
    for i in st:
        val = ord(i) - ord("a")
        countArr[val] += 1
        if(countArr[val] % 2 == 0):
            countOdd -= 1
        else:
            countOdd += 1
    return countOdd == 1 or countOdd == 0

def checkPalindrome(st):
    bitVector = ["0"]*26
    for i in st:
        val = ord(i) - ord("a")
        if(bitVector[val] == "0"):
            bitVector[val] = "1"
        else:
            bitVector[val] = "0"
    checker = int("".join(bitVector), 2)
    return checker & checker-1 == 0
    
st = input()
print(checkPalindrome(st))
