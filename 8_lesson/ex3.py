boxes = [
"іграшка",
"книга",
"одяг",
"ключ",
"лист",
"одяг",
"книга",
"зошит",
"фрукти",
]

search_value = input("Що ви хочете знайти? введіть "
"ТІЛЬКИ першу літеру ")

for box in boxes:
     if box.startswith("к"):
        continue
     elif box.startswith(search_value):
         print(box)
         break
else:
    print("Нічого не знайдено")

