print("Welcome to Riri's Palindrome Checker!")

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    text= text.lower().replace(" ", "") #ignores case & spaces
    return text == text[::-1]
#Ask multiple times in a loop until user wants to quite
while True: 
    text = input("Enter a string (or type 'exit' to quit): ")
    if text.lower() == "exit": #user can stop by typing exit
        print("Goodbye...")
        break
    
    if is_palindrome(text): 
        print("✅ It's a palindrome!")
    else: 
        print("❌ NOT a palindrome")

