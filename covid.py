age = input("Are you a cigarette addict older than 75 years old? (Respond with Yes/No): ").lower()
chronic = input("Do you have a severe chronic disease? (Respond with Yes/No): ").lower()
immune = input("Is your immune system too weak? (Respond with Yes/No): ").lower()

risk = "yes" in [age, chronic, immune]

print(risk)