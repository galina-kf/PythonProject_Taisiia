words = ["sun", "moon", "earth", "mars",
         "venus", "jupiter"]

cap_words = {word.upper() for word in words}
print(cap_words)

word_dict = {word: word[0] for word in words}
print(word_dict)