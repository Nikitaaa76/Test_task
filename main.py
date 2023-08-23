from user_interface import get_info
from file_writting import writing_txt


if __name__ == "__main__":

    def find_entries(attributes):
        """
        Функция find_entries(attributes) принимает на вход словарь attributes,
        содержащий характеристики записей, которые нужно найти.
        Функция ищет все записи в списке entries, которые соответствуют переданным характеристикам,
        и возвращает список строк с информацией о найденных записях.
        Если ни одна запись не найдена, функция вернет пустой список.

        """
        results = []
        for entry in entries:
            match = True
            for key, value in attributes.items():
                if key in entry and str(entry[key]) != value:
                    match = False
                    break
            if match:
                result_str = ""
                for key, value in entry.items():
                    if key == "first_name":
                        result_str += f"Имя: {value}\n"
                    elif key == "last_name":
                        result_str += f"Фамилия: {value}\n"
                    elif key == "patronymic_name":
                        result_str += f"Отчество: {value}\n"
                    elif key == "firm":
                        result_str += f"Название организации: {value}\n"
                    elif key == "work_phone_number":
                        result_str += f"Рабочий номер телефона: {value}\n"
                    elif key == "phone_number":
                        result_str += f"Личный номер телефона: {value}\n"
                results.append(result_str.rstrip())
        return results


    def show_info(page_num):
        """
        Функция show_info(page_num) отображает информацию о контактах на указанной странице
        и предоставляет пользователю возможность редактировать записи,
        сохранять их в txt файл или вернуться в главное меню.
        Если пользователь выбирает редактирование записи,
        функция вызывает функцию get_info() для получения новой информации
        о контакте и обновляет соответствующую запись.
        Если пользователь выбирает сохранение записей в txt файл,
        функция вызывает функцию writing_txt() для сохранения записей
        в файл contacts.txt.
        :return: None
        """
        entries = pages.get(page_num, [])
        if entries:
            print(f"Страница {page_num}:")
            for entry in entries:
                print(f"Имя: {entry['first_name']}\n"
                      f"Фамилия: {entry['last_name']}\n"
                      f"Отчество: {entry['patronymic_name']}\n"
                      f"Название организации: {entry['firm']}\n"
                      f"Номер рабочего телефона: {entry['work_phone_number']}\n"
                      f"Номер личного телефона: {entry['phone_number']}\n"
                      )
                option = input(
                    "Выберите 1 для редактирования 2 для сохранения в txt файл или 0 для выхода в главное меню: ")
                print(Separator)
                if option == "0":
                    return

                elif option == "2":
                    writing_txt(entries)
                    print("Запись успешно сохранены в файл contacts.txt.")

                elif option == "1":
                    try:
                        entry_num = int(option) - 1
                        entry = entries[entry_num]
                        print(f"Редактирование записи {entry_num + 1}:")
                        info = get_info()
                        entry.update({
                            "first_name": info[0],
                            "last_name": info[1],
                            "patronymic_name": info[2],
                            "firm": info[3],
                            "work_phone_number": info[4],
                            "phone_number": info[5]
                        })
                        pages[page_num] = entries
                        print("Запись успешно обновлена.")
                    except (ValueError, IndexError):
                        print("Некорректный выбор. Попробуйте еще раз.")


    pages = {
        1: [],
    }
    Separator = '------------------------------------------'

    while True:
        # main menu
        print(Separator)
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Ввести информацию')
        print('2 - Показать информацию')
        print('3 - Поиск записей по характеристикам')
        print('0 - Завершить работу')

        try:
            option = int(input('Введите номер пункта меню: '))
            if option == 0:
                break
            if option == 1:
                info = get_info()
                # Ищем первую пустую страницу
                found_empty_page = False
                for page_num, entries in pages.items():
                    if not entries:
                        found_empty_page = True
                        pages[page_num].append({
                            "first_name": info[0],
                            "last_name": info[1],
                            "patronymic_name": info[2],
                            "firm": info[3],
                            "work_phone_number": info[4],
                            "phone_number": info[5]
                        })
                        print(f"Информация успешно добавлена на страницу {page_num}")
                        break

                # Если все страницы заполнены, создаем новую
                if not found_empty_page:
                    new_page_num = len(pages) + 1
                    pages.setdefault(new_page_num, [])
                    pages[new_page_num].append({
                        "first_name": info[0],
                        "last_name": info[1],
                        "patronymic_name": info[2],
                        "firm": info[3],
                        "work_phone_number": info[4],
                        "phone_number": info[5]
                    })
                    print(f"Информация успешно добавлена на новую страницу {new_page_num}")

            if option == 2:
                print(Separator)
                print("Доступные страницы:")
                for page_num in pages.keys():
                    print(f"Страница {page_num}")
                page_num = int(input("Введите номер страницы: "))
                print(Separator)
                show_info(page_num)

            if option == 3:
                print(Separator)
                print("Поиск записей по нескольким характеристикам")
                attributes = {}
                work_phone_number = input("Введите номер рабочего телефона: ")
                if work_phone_number:
                    attributes["work_phone_number"] = work_phone_number
                phone_number = input("Введите номер телефона: ")
                if phone_number:
                    attributes["phone_number"] = phone_number
                firm = input("Введите название организации: ")
                if firm:
                    attributes["firm"] = firm
                results = find_entries(attributes)
                if results:
                    print(Separator)
                    print("Найдены следующие записи:")
                    for result in results:
                        print(result)
                else:
                    print("Записей не найдено.")
        except:
            print("Введите цифру")
