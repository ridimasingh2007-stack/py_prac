import requests 

# letting user choose the amount of advice they want
num_advices = int(input("How many advice would you like?💡: "))
advices = []
favorites = []

print("\n🌟Here are your advices:\n")
for i in range(num_advices):
    #Fetch random advice
    res = requests.get("https://api.adviceslip.com/advice")
    advice = res.json()["slip"]["advice"]
    advices.append(advice)
    print(f"\n{i+1}. 🌟 \"{advice}\"")

#Emoji rating
for i, advice in enumerate(advices):
    rating = input("Rate this advice!🤩=Great 😁=Nice 😐=neutral : ") 
    print(f"You rated advice #{i+1} as: {rating}")

# Option to save
    save = input("Do you want to save this advice? (y/n): ")
    if save.lower() == "y":
        favorites.append(advice)

# Save to file
if favorites:
    with open("favorite_advices.txt", "w") as f:
        for adv in favorites:
            f.write(adv + "\n")
    print("🎉 Your favorite advices are saved in 'favorite_advices.txt'!")      

print("Thanks for getting inspired! 🚀✨")
