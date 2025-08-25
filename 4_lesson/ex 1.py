favorite_icecream_marichka = {"ванільне", "шоколадне", "полуничне", "фісташкове"}
favorite_icecream_taras = {"шоколадне", "фісташкове", "мангове", "лимонне"}

favorite_icecream_marichka.update(favorite_icecream_taras)
#print(favorite_icecream_marichka)

#print(f"{favorite_icecream_marichka =}")
#print(f"{favorite_icecream_taras =}")

#favorite_icecream_taras.discard("вишневе") #no error
#favorite_icecream_taras.remove("лимонне") #error
#favorite_icecream_taras.pop() #random delete, error if not in list

#print(favorite_icecream_marichka.symmetric_difference(favorite_icecream_taras))
print(favorite_icecream_marichka-favorite_icecream_taras)