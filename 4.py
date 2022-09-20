def is_palindrome(kata):
    x = list(kata)
    y = list(reversed(x))
    if(x==y):
        return True
    return False

print(is_palindrome('malam'))
