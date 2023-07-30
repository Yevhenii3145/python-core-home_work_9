import typing

PHONE_BOOK: dict[str, str] = {}


def input_error(func: typing.Callable) -> typing.Callable:

    def inner(*args: str, **kwargs: dict) -> str:

        if len(args) == 2 and not args[1].isdigit():
            return "DECORATOR Phone number must consist only of numbers"

        try:
            result = func(*args, **kwargs)
            return f"RESULT: {result}"

        except ValueError as error:
            return f"DECORATOR An error has occurred. Er: {error}"
        except IndexError as error:
            return f"DECORATOR Index not in range.Er: {error}"
        except KeyError as error:
            return f"DECORATOR No such KEY.Er: {error}"
        except TypeError as error:
            return f"DECORATOR Input correct all required arguments.Er: {error}"

    return inner


def say_hello() -> str:
    return "How can I help you?"


@input_error
def add_user(name: str, phone_num: str) -> str:

    if PHONE_BOOK.get(name):
        raise ValueError(
            f"User '{name}' already in phone book.Try another command or another name")

    PHONE_BOOK.update({name: phone_num})

    return f"In phone book added user '{name}' with phone '{phone_num}'"


@input_error
def change_contact(name: str, phone_num: str) -> str:

    if PHONE_BOOK.get(name):
        PHONE_BOOK[name] = phone_num
    else:
        raise ValueError(f"User '{name}' is not in phone book")

    return f"In phone book changed phone number of user '{name}' to '{phone_num}'"


@input_error
def get_phone(name: str) -> str:

    if PHONE_BOOK.get(name):
        target_num = PHONE_BOOK[name]
    else:
        raise ValueError(f"User '{name}' is not in phone book.")

    return f"Target phone number for user '{name}'  is '{target_num}'"


def show_all() -> str:
    return f"show_all {PHONE_BOOK}"


COMANDS: dict[str, typing.Callable] = {
    'hello': say_hello,
    'add': add_user,
    'change': change_contact,
    'phone': get_phone,
    'show all': show_all,
}


def get_handler(comand: str) -> typing.Callable:
    return COMANDS[comand]


def main() -> None:
    launch = 0

    while True:
        if launch == 0:
            print("I'am a Bot")
            launch = 1

        user_input = input("Please input a comand: ")
        user_input = user_input.lower()

        if "show all" in user_input:
            comand = "show all"
            handler = get_handler(comand)
            print(handler())
            continue

        elif "good bye" in user_input:
            print("Good bye!")
            break

        list_of_request = user_input.strip().split(' ')
        comand = list_of_request[0]
        request_data = list_of_request[1:]

        if request_data:
            if len(request_data) >= 2 and request_data[len(request_data)-1].isdigit():
                name = (" ").join(request_data[:len(request_data) - 1])
                phone = request_data[-1]
                request_data = [name, phone]

            elif request_data[len(request_data)-1].isalpha():
                name = (" ").join(request_data[:])
                request_data = [name]

        if comand in ("close", "exit"):
            print("Good bye!")
            break

        try:
            handler = get_handler(comand)
            print(handler(*request_data))
        except KeyError as error:
            print(f"I don't know such a command.Er: {error}")
        continue


if __name__ == "__main__":
    main()
