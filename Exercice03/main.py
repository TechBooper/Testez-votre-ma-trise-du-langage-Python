words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = "aeiou"
result = [(word, sum(1 for letter in word if letter.lower() in vowels)) for word in words]

print("Liste des mots :")
for word in words:
    print(word)

print("\nListe des mots avec le nombre de voyelles :")
print(result)
