from collections import deque


def is_palindrome(text):
    #sanitize string
    text = text.replace(" ", "").lower()

    d = deque(text)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


text = input("Enter string: ")

if is_palindrome(text):
    print("This is palindrome.")
else:
    print("This isn't palindrome.")