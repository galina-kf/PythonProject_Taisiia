#text = "Їде велосипедист"
#print(text.split()[1])

#print(list(range(15, 27)))
#print(list(range(1, 11, -1)))

def split_text(text: str) -> list[str]:
    split_chars = "\n\t.!?-,"
    for char in split_chars:
        text = text.replace(old=char, new= " ")
    print(text)
    words = text.split(" ")
    words= [w for w in words if w !=""]
    return words