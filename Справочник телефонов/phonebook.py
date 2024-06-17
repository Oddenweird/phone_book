def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while choice!=7:
        if choice == 1:
            for record in phone_book:
                print(', '.join(record.values()))
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice == 6:
            line_number = int(input('Введите номер строки для копирования: '))
            copy_data(phone_book, line_number)
        elif choice==7:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        choice = show_menu()

def find_by_lastname(phone_book, last_name):
    # Поиск всех записей с заданной фамилией
    found_records = [record for record in phone_book if record['фамилия'].lower() == last_name.lower()]
    if found_records:
        return '\n'.join([', '.join(record.values()) for record in found_records])
    else:
        return 'Запись не найдена.'

def change_number(phone_book, last_name, new_number):
    # Флаг для отслеживания успешности операции
    found = False
    for record in phone_book:
        if record['фамилия'].lower() == last_name.lower():
            record['телефон'] = new_number
            found = True
    if found:
        return 'Номер успешно изменён.'
    else:
        return 'Абонент с такой фамилией не найден.'

def show_menu():
    print("\nВыберете необходимое действие:\n"
          "1. Отобразить телефонный справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента и исправить номер телефона\n"
          "4. Удалить абонента\n"
          "5. Найти по номеру телефона\n"
          "6. Копирование строки в новый справочник\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book = []
    fields = ['фамилия', 'имя', 'телефон', 'описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def copy_data(phone_book, line_number):
    if 0 <= line_number < len(phone_book):
        record = phone_book[line_number]
        write_txt('another_phonebook.txt', [record])
    else:
        print('Некорректный номер строки')

def delete_by_lastname(last_name):
    global phone_book  # Объявляем phone_book глобальной переменной
    phone_book = [record for record in phone_book if record['фамилия'].lower() != last_name.lower()]
    return 'Записи с фамилией "{}" удалены.'.format(last_name)

def find_by_number(phone_book, number):
    # Поиск всех записей с заданным номером телефона
    found_records = [record for record in phone_book if record['телефон'] == number]
    if found_records:
        return '\n'.join([', '.join(record.values()) for record in found_records])
    else:
        return 'Запись с таким номером не найдена.'

def add_user(phone_book, first_name, last_name, number):
    # Добавление нового пользователя в телефонный справочник
    new_record = {'имя': first_name, 'фамилия': last_name, 'телефон': number}
    phone_book.append(new_record)
    return 'Новый абонент "{} {}" добавлен.'.format(first_name, last_name)

work_with_phonebook()