def is_palindrome(text):
    return text.lower() == text[::-1].lower()


print(is_palindrome("Kajak"))