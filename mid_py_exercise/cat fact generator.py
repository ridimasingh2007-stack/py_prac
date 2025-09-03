
# 1.. Cats facts generator
import requests
def get_fact():
    """" Fetch and display a cat fact from the API."""
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()

    print("\n🐱 Here is you cat fact: ")
    print(data["fact"])
    


print("===Cat fact generator===")
print("Press Enter to get a new fact, or type 'q' to quit.\n")

while True:
    choice = input("your choice: ")
    if choice.lower() == "q": 
        print("\nGoodbye! Come back for more facts🐾")
        break
    else: 
        get_fact()