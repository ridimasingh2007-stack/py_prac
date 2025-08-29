print("Welcome to riri's palindrom checker")
 
def is_palindrom(text):
    length = len(text)

    for i in range( 0, length // 2):
        if (text[i] != text[length-i-1]):
            return False
    return True
Str1 = input("Enter the first string you want to check: " )
print(is_palindrom(Str1))

Str2 = input("Enter the second string you want to check: ")
print(is_palindrom(Str2))