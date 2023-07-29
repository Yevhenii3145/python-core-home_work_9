PHONE_BOOK = {}


def input_error(func):

    def inner(list_of_request):

        if func.__name__ == "get_phone" and len(list_of_request) != 1:
            print("DECORATOR Please just enter 1 arg: correct name of user")
            print("DECORATOR Trye again")
            exit  # здесь не сработал почему-то
            return

        if func.__name__ != "get_phone":
            if len(list_of_request) < 2 or len(list_of_request) > 2:
                print("DECORATOR Please enter 2 args: correct name and phone number")
                print("DECORATOR Trye again")
                exit  # здесь не сработал почему-то
                return

            elif len(list_of_request) == 2:
                if not list_of_request[1].isdigit():
                    print("DECORATOR Phone number must consist only of numbers")
                    return

        try:
            result = func(list_of_request)
            print("RESULT", result)
            return result

        except ValueError as error:
            print(f"DECORATOR An error has occurred. Er: {error}")
        except IndexError as error:
            print(f"DECORATOR Index not in range.Er: {error}")
        except KeyError as error:
            print(f"DECORATOR No such KEY.Er: {error}")

    return inner


def say_hello():
    print("How can I help you?")


@input_error
def add_user(list_of_request):
    name = list_of_request[0]
    phone_num = list_of_request[1]

    if PHONE_BOOK.get(name):
        raise ValueError(
            f"User {name} already in phone book.Try another command or another name")

    PHONE_BOOK.update({name: phone_num})

    print("add_user", PHONE_BOOK)
    return f"In phone book added user {name} phone {phone_num}"


@input_error
def change_contact(list_of_request):
    name = list_of_request[0]
    phone_num = list_of_request[1]

    if PHONE_BOOK.get(name):
        PHONE_BOOK[name] = phone_num
    else:
        raise ValueError(f"User {name} is not in phone book")

    print("change_contact", PHONE_BOOK)
    return f"In phone book changed phone number of user {name} to {phone_num}"


@input_error
def get_phone(list_of_request):
    name = list_of_request[0]

    try:
        target_num = PHONE_BOOK[name]
        print("get_phone", target_num)
        return f"Target phone number for user {name}  is {target_num}"
    except ValueError as error:
        print(f"User {name} is not in phone book.Er: {error}")


def show_all():
    print("show_all", PHONE_BOOK)


COMANDS = {
    'hello': say_hello,
    'add': add_user,
    'change': change_contact,
    'phone': get_phone,
    'show_all': show_all,
}


def get_handler(comand):
    return COMANDS[comand]


def main():

    while True:
        print("I'am a Bot")

        user_input = input("Please input a comand: ")
        user_input = user_input.lower()

        if "show all" in user_input:
            comand = "show_all"
            handler = get_handler(comand)
            handler()
            continue
        elif "good bye" in user_input:
            print("Good bye!")
            break

        user_input_list = user_input.split(" ")
        comand = user_input_list[0]
        if comand in ("close", "exit"):
            print("Good bye!")
            break

        list_of_request = user_input_list[1:]

        try:
            handler = get_handler(comand)
            handler = handler(list_of_request) if len(
                list_of_request) > 0 else handler()
        except KeyError as error:
            print(f"I don't know such a command.Er: {error}")
        continue


if __name__ == "__main__":
    main()
