num = 121
def isPalindrome(num): 
    s = str(num) # it converts to string
    return s == s[::-1] # if it is Same it is Palindrome
print(isPalindrome(num))