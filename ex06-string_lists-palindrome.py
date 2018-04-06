"""
https://www.practicepython.org

Exercise 6: String Lists
2 chilis

Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)
"""

def palindrome_checker(s1):
    for i in range(int(len(s1)/2)):
        if s1[i] != s1[len(s1)-i-1] :
            return(False)
    return(True)


s1 = input("Enter some text:  ")
if palindrome_checker(s1.lower()):
    print("'" + s1 + "' is a palindrome")
else:
    print("'" + s1 + "' is not a palindrome")
