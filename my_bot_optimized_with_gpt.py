response = """
Ваш код выглядит хорошо и хорошо структурирован! Однако, есть несколько моментов,
которые можно оптимизировать:

Обработка ввода имени и номера телефона в функциях add_user, change_contact
и get_phone:
Вы можете обработать ввод имени и номера телефона один раз в основном цикле
вместо того, чтобы делать это в каждой функции-обработчике. Это позволит
уменьшить дублирование кода.

Обработка команды "show all":
В функции main, вы проверяете наличие "show all" в пользовательском вводе и
затем выполняете замену этой команды на пустую строку и разбиваете её на части.
Это можно упростить, так как у вас уже есть отдельная функция show_all, которая
выполняет эту команду. Вы можете просто вызвать show_all() вместо обработки этой
команды отдельно.

Избавление от переменной launch:
Переменную launch можно убрать, так как она используется только для вывода
"I'm a Bot" в начале программы. Вы можете просто вывести это сообщение без
использования переменной.

Вот оптимизированный код:
Я оптимизировал код, чтобы убрать некоторые дублирования и улучшить его
читаемость. Теперь ваш бот должен работать так же, как и ранее, но с улучшенной
структурой. Если у вас возникнут вопросы или потребуется дополнительная помощь,
пожалуйста, дайте мне знать. Удачи вам!

До чего дошёл прогресс - до невиданных чудес ;)
"""
import typing

PHONE_BOOK: dict[str, str] = {}


def input_error(func: typing.Callable) -> typing.Callable:
    def inner(*args: str, **kwargs: dict) -> str:
        try:
            return f"{func(*args, **kwargs)}"
        except (KeyError, ValueError, IndexError, TypeError) as error:
            return f"DECORATOR An error has occurred. Er: {error}"
    return inner


@input_error
def say_hello() -> str:
    return "How can I help you?"


@input_error
def add_user(name: str, phone_num: str) -> str:
    if PHONE_BOOK.get(name):
        raise ValueError(f"User '{name}' already in phone book. Try another command or another name")
    PHONE_BOOK[name] = phone_num
    return f"In phone book added user '{name}' with phone '{phone_num}'"


@input_error
def change_contact(name: str, phone_num: str) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in phone book")
    PHONE_BOOK[name] = phone_num
    return f"In phone book changed phone number of user '{name}' to '{phone_num}'"


@input_error
def get_phone(name: str) -> str:
    if name not in PHONE_BOOK:
        raise ValueError(f"User '{name}' is not in phone book.")
    return f"Target phone number for user '{name}' is '{PHONE_BOOK[name]}'"


@input_error
def show_all() -> str:
    if not PHONE_BOOK:
        return "The phone book is empty."
    result = "show_all:\n"
    for name, phone in PHONE_BOOK.items():
        result += f"{name} - {phone}\n"
    return result


@input_error
def to_close() -> str:
    return "Good bye!"


def default_handler(*args) -> str:
    return f"I don't know such a command"


COMANDS: dict[str, typing.Callable] = {
    'hello': say_hello,
    'add': add_user,
    'change': change_contact,
    'phone': get_phone,
    'show all': show_all,
    'close': to_close,
}


def get_handler(comand: str) -> typing.Callable:
    return COMANDS.get(comand, default_handler)


def main() -> None:
    print("I'm a Bot")
    while True:
        user_input = input("Please input a command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
            handler = get_handler('close')
            request_data = user_input.replace('good bye', "").replace("close","").replace("exit","").split()
            print(handler(*request_data))
            break

        elif 'show all' in user_input:
            handler = get_handler('show all')
            request_data = user_input.replace('show all', "").split()
            print(handler(*request_data))
            continue

        list_of_request = user_input.strip().split(' ')
        comand = list_of_request[0]
        request_data = list_of_request[1:]

        if not request_data and comand == "show":
            comand = "show all"

        if request_data and request_data[-1].isdigit():
            name = " ".join(request_data[:-1])
            phone = request_data[-1]
            request_data = [name, phone]
        elif request_data and request_data[-1].isalpha():
            name = " ".join(request_data[:])
            request_data = [name]

        handler = get_handler(comand)
        print(handler(*request_data))


if __name__ == "__main__":
    main()
