import requests
def get_jokes():
    """Fecth and display a random joke from the API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()

    print("\n😂 Here's your joke:")
    print(data["setup"])
    print(data["punchline"])

# loop

print("===Random Joke Generator ===")
print("Press Enter to get a new joke, or tyoe 'q' to quit.\n")

while True:
    choice = input("your choice: ")
    if choice.lower() == "q": 
        print("\nGoodbye! Come back for more laughs")
        break
    else: 
        get_jokes()





print(response.status_code)
print(response.text)