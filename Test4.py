#Test Case 4
def checkPalindrome(a):
    return a[:int(len(a)/2)] == "".join(list(reversed(a[len(a)-int(len(a)/2):])))
print(checkPalindrome("racecar")) 
print(checkPalindrome("python"))  
print(checkPalindrome("habibah")) 