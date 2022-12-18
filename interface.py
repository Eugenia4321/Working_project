from colorama import init
init()
from colorama import Fore, Back, Style

def hello():
    '''Функция приветствия'''
    print(Fore.CYAN + Style.NORMAL + 'Вас приветствует телефонная книга' + Style.RESET_ALL)

def main_menu():
    ''' Функция главного меню. Возвращает номер пункта меню, который ввёл пользователь'''
    print(Fore.CYAN + Style.NORMAL + '\nМЕНЮ' + Style.RESET_ALL)
    print(Fore.GREEN + Style.NORMAL + '1. Добавить запись' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '2. Найти номер по фамилии' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '3. Найти номер по имени' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '4. Поиск по номеру телефона' + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.NORMAL + '5. Показать все контакты' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + '6. Редактировать запись' + Style.RESET_ALL)
    print(Fore.RED + Style.NORMAL + '7. Удалить запись' + Style.RESET_ALL)
    print(Fore.WHITE + Style.NORMAL + '8. Выйти из программы\n' + Style.RESET_ALL)
    
def menu_item():
    ''' Функция выбора пункта меню. Возвращает номер пункта меню, который ввёл пользователь'''
    n = int(input(Fore.CYAN + Style.NORMAL + 'Выберите пункт из меню: ' + Style.RESET_ALL))
    return n

def get_surname():
    '''Запрашивает у пользовтеля фамилию'''
    surname = input(Fore.CYAN + Style.NORMAL + 'Введите фамилию: ' + Style.RESET_ALL).title()
    return surname

def get_name():
    '''Запрашивает у пользовтеля имя'''
    name = input(Fore.CYAN + Style.NORMAL + 'Введите имя: ' + Style.RESET_ALL).title()
    return name

def get_tel_num():
    '''Запрашивает у пользовтеля телефон'''
    number = input(Fore.CYAN + Style.NORMAL + 'Введите номер телефона: ' + Style.RESET_ALL).replace(" ", "")
    return number

def get_comment():
    '''Запрашивает у пользовтеля комментарий'''
    comment = input(Fore.CYAN + Style.NORMAL + 'Введите комментарий: ' + Style.RESET_ALL).title()
    return comment

def get_new_surname():
    '''Запрашивает у пользовтеля новую фамилию'''
    new_surname = input(Fore.CYAN + Style.NORMAL + 'Введите новую фамилию: ' + Style.RESET_ALL).title()
    return new_surname

def get_new_name():
    '''Запрашивает у пользовтеля новое имя'''
    new_name = input(Fore.CYAN + Style.NORMAL + 'Введите новое имя: ' + Style.RESET_ALL).title()
    return new_name

def get_new_tel_num():
    '''Запрашивает у пользовтеля новый телефон'''
    new_number = input(Fore.CYAN + Style.NORMAL + 'Введите новый номер телефона: ' + Style.RESET_ALL).replace(" ", "")
    return new_number

def get_new_comment():
    '''Запрашивает у пользовтеля новый комментарий'''
    new_comment = input(Fore.CYAN + Style.NORMAL + 'Введите новый комментарий: ' + Style.RESET_ALL).title()
    return new_comment

def error_name():
    '''Печатает ошибку, если имя введено неверно'''
    print(Fore.RED + Style.NORMAL + 'Имя введено неверно. Попробуйте ещё раз' + Style.RESET_ALL)

def error_surname():
    '''Печатает ошибку, если фамилия введена неверно'''
    print(Fore.RED + Style.NORMAL + 'Фамилия введена неверно. Попробуйте ещё раз' + Style.RESET_ALL)

def error_tel_num():
    '''Печатает ошибку, если номер телефона введен неверно'''
    print(Fore.RED + Style.NORMAL + 'Номер телефона введён неверно. Попробуйте ещё раз' + Style.RESET_ALL)

def error_comment():
    '''Печатает ошибку, если комментарий введен неверно'''
    print(Fore.RED + Style.NORMAL + 'Неверный формат комментария/превышен лимит. Попробуйте ещё раз' + Style.RESET_ALL)

def error_menu_item():
    '''Печатает ошибку, если введено число, которого нет в меню'''
    print(Fore.RED + Style.NORMAL + '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.' + Style.RESET_ALL)

def error_no_contact():
    '''Печатает ошибку, если нет совпадений'''
    print(Fore.RED + Style.NORMAL + 'У вас в книге нет такого абонента' + Style.RESET_ALL)

def question_to_add():
    '''Спрашивает у пользователя хочет ли он ввести ещё один контакт'''
    question = input(Fore.CYAN + Style.NORMAL + 'Хотите ввести еще один контакт? Y/N: ' + Style.RESET_ALL)
    return question
            
def create_success():
    '''Печатает об успешном создании контакта'''
    print(Fore.GREEN + Style.NORMAL + 'Контакт успешно создан.' + Style.RESET_ALL)

def update_success():
    '''Печатает об успешном изменении контакта'''
    print(Fore.GREEN + Style.NORMAL + 'Контакт успешно изменён.' + Style.RESET_ALL)

def top_line():
    '''Печатает шапку для найденной строки контактов'''
    print("---"*20)
    print('Фамилия|\tИмя|\tНомер_Телефона|\tКомментарий|')
    print("---"*20)

def result_search():
    '''Печатает результат поиска по параметру'''
    print(Fore.CYAN + Style.NORMAL + 'По искомым параметрам нашлись следующие контакты:\n' + Style.RESET_ALL)

def result_read():
    '''Выводит весь список контактов'''
    print(Fore.CYAN + Style.NORMAL + f'В вашем справочнике следующие контакты:\n' + Style.RESET_ALL)

def menu_item_options():
    '''Функция печатает предлагаемые опции выбранного пункта меню'''
    print(Fore.BLUE + Style.NORMAL + '1. Найти номер по фамилии' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '2. Найти номер по имени' + Style.RESET_ALL)
    print(Fore.BLUE + Style.NORMAL + '3. Поиск по номеру телефона' + Style.RESET_ALL)

def bye():
    '''Выводит сообщение о завершении работы телефонного справочника.
    '''
    print(Fore.CYAN + Style.NORMAL + 'Спасибо за работу!' + Style.RESET_ALL)