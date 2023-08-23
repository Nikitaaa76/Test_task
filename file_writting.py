def writing_txt(entries):
    """
    Функция writing_txt(entries) записывает информацию о контактах
    в текстовый файл "contacts.txt". Параметр entries является списком словарей,
    где каждый словарь содержит информацию об одном контакте. Функция записывает
    в файл следующую информацию о каждом контакте: имя,
    фамилию, отчество, название организации,
    номер рабочего телефона и номер личного телефона
    Функция не возвращает никакого значения.

    """
    with open("contacts.txt", "w") as file:
        for entry in entries:
            file.write(f"Имя: {entry['first_name']}\n"
                       f"Фамилия: {entry['last_name']}\n"
                       f"Отчество: {entry['patronymic_name']}\n"
                       f"Название организации: {entry['firm']}\n"
                       f"Номер рабочего телефона: {entry['work_phone_number']}\n"
                       f"Номер личного телефона: {entry['phone_number']}\n\n"
                       )
