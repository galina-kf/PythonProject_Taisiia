favorite_icecream_marichka = {"ванільне", "шоколадне", "полуничне", "фісташкове"}
favorite_icecream_taras = {"шоколадне", "фісташкове", "мангове", "лимонне"}

#1
#1.1
new_icecream_marichka = input("Add icecream for marichka:")
favorite_icecream_marichka.add(new_icecream_marichka)

#1.2
favorite_icecream_taras.discard("вишневе")
favorite_icecream_taras.remove("лимонне")

#1.3
favorite_icecream_marichka.pop()
print(favorite_icecream_marichka)

#2
#2.1
print(favorite_icecream_marichka | favorite_icecream_taras) #or
print(favorite_icecream_marichka.union(favorite_icecream_taras))

#2.2
print(favorite_icecream_marichka & favorite_icecream_taras) #or
print(favorite_icecream_marichka.intersection(favorite_icecream_taras))

#2.3
print(favorite_icecream_marichka-favorite_icecream_taras)

#2.4
favorite_icecream_marichka.intersection_update(favorite_icecream_taras)
print(f"{favorite_icecream_marichka =}")

#2.5
favorite_icecream_taras.update(favorite_icecream_marichka)
print(f"{favorite_icecream_taras =}")



