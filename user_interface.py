def get_info():
    """
    Функция get_info() запрашивает у пользователя информацию о его имени,
    фамилии, отчестве, названии организации, номерах рабочего и личного телефонов.
    При этом происходит проверка корректности ввода данных: имя,
    фамилия и отчество должны состоять только из букв,
    номера телефонов должны содержать 11 цифр.
    Функция возвращает список с полученной информацией.

    """
    info = []
    while True:
        first_name = input('Введите имя: ')
        if first_name.isalpha():
            info.append(first_name.capitalize())
            break
        else:
            print('Имя должно содержать только буквы, попробуйте ещё раз.')

    while True:
        last_name = input('Введите фамилию: ')
        if last_name.isalpha():
            info.append(last_name.capitalize())
            break
        else:
            print('Фамилия должна содержать только буквы, попробуйте ещё раз.')

    while True:
        patronymic_name = input('Введите отчество: ')
        if patronymic_name.isalpha():
            info.append(patronymic_name.capitalize())
            break
        else:
            print('Отчество должно содержать только буквы, попробуйте ещё раз.')

    firm = input('Введите название организации: ')
    info.append(firm)
    work_phone_number = ''
    phone_number = ''
    valid = False

    while not valid:
        work_phone_number = input('Введите номер рабочего телефона : ')
        if len(work_phone_number) != 11:
            print('В номере телефона должно быть 11 цифр, попробуйте ещё раз.')
        else:
            try:
                work_phone_number = int(work_phone_number)
                valid = True
            except:
                print('Номер телефона должен состоять только из цифр, попробуйте ещё раз.')

    valid = False

    while not valid:
        phone_number = input('Введите номер личного телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр, попробуйте ещё раз.')
        else:
            try:
                phone_number = int(phone_number)
                valid = True
            except:
                print('Номер телефона должен состоять только из цифр, попробуйте ещё раз.')

    info.append(work_phone_number)
    info.append(phone_number)

    return info