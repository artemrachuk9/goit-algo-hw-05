# MYHOMETASK 3
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
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
def show_all(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result) if result else "No contacts found."

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            raw_data = input("Enter the argument for the command\nEnter a command: ")
            args = raw_data.split()
            print(add_contact(args, contacts))
        elif command == "phone":
            raw_data = input("Enter the argument for the command\nEnter a command: ")
            args = raw_data.split()
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["exit", "close"]:
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()