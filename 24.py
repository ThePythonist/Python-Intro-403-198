word = input("Enter any word : ")
words = ("pop", "dad", "radar")

if word == word[::-1]:
    words += (word,)

print(words)
