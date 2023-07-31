def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Error: {e}")
    return wrapper

def hello_handler():
    return "How can I help you?"

@input_error
def add_handler(contact_dict, name, phone):
    contact_dict[name] = phone
    return f"Added new contact: {name} - {phone}"

@input_error
def change_handler(contact_dict, name, phone):
    if name in contact_dict:
        contact_dict[name] = phone
        return f"Changed phone for {name}: {phone}"
    else:
        raise ValueError(f"Contact '{name}' not found")

@input_error
def phone_handler(contact_dict, name):
    if name in contact_dict:
        return f"Phone number for {name}: {contact_dict[name]}"
    else:
        raise ValueError(f"Contact '{name}' not found")

def show_all_handler(contact_dict):
    result = "Contacts:\n"
    for name, phone in contact_dict.items():
        result += f"{name} - {phone}\n"
    return result

def main():
    contact_dict = {}
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print(hello_handler())
        elif user_input.startswith("add"):
            _, name, phone = user_input.split(maxsplit=2)
            print(add_handler(contact_dict, name, phone))
        elif user_input.startswith("change"):
            _, name, phone = user_input.split(maxsplit=2)
            print(change_handler(contact_dict, name, phone))
        elif user_input.startswith("phone"):
            _, name = user_input.split(maxsplit=1)
            print(phone_handler(contact_dict, name))
        elif user_input == "show all":
            print(show_all_handler(contact_dict))
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
