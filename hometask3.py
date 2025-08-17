def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to {new_phone}."
    else:
        raise KeyError


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_command(user_input):
    parts = user_input.strip().split()
    if not parts:
        return None, []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_command(user_input)

        if command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "hello":
            print("How can I help you?")
        elif command in ["exit", "close"]:
            print("Goodbye!")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
