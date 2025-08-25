#повторення
name = "Ivan"
lower_name = name.lower() # ivan
upper_name = name.upper() # IVAN
lstrip_name = name.lstrip() # видаляє пробіли зліва
rstrip_name = name.rstrip() # видаляє пробіли з правої частини
strip_name = name.strip() # видаляє пробіли з обох боків

mixed_case_text = "СьОгОдНі На ВуЛиЦі Дощ. "
title_text = mixed_case_text.title() # Сьогодні На Вулиці Дощ.
capitalized_text = mixed_case_text.capitalize() # Сьогодні на вулиці дощ.

text = "ПРИВІТ. сьогодні сніг, пасмурно"
replaced_text = text.replace( "Сьогодні","Завтра буде") # "ПРИВІТ. Завтра буде
splitted_text = text.split(",") # ділить на підрядки, ["ПРИВІТ. сьогодні сніг", "пасмурно
is_string_start_with = name.strip().startswith("Iv") # Чи починається рядок з підрядка (Три
is_string_end_with = text.strip() .endswith("сніжно") # Чи закінчується редок на підрядок СТ

age = 25
formatted = f"Привіт. Мене звати {name.strip()}. Мій вік {age}"
print (formatted)

not_formatted = "Привіт. Мене звати name.strip(). Мій вік age"
print (not_formatted)