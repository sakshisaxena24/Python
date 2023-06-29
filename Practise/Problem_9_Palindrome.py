#Problem 9:Leetcode : Palindrome Number

class Solution(object):
    def isPalindrome(x):
        rev = 0
        original = x
        while (x > 0):
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
        if (original == rev):
            return True
        else:
            return False

    number = int(input("Enter you number"))
    print(number)
    flag = isPalindrome(number)
    print(flag)

    if (flag == True):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")