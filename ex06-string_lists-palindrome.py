def palindrome_checker(s1):
    is_palindrome = 1
    i = 0
    while i <= len(s1)/2 and is_palindrome:
        if s1[i] != s1[len(s1)-i-1] :
            is_palindrome = 0
        i += 1
    return(is_palindrome)

s1 = str(input("Enter a string "))
if palindrome_checker(s1.lower()):
    print(s1 + " is a palindrome")
else:
    print(s1 + " is not a palindrome")
