
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

'''
def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Невірна кількість аргументів. Потрібно вказати ім'я та телефон.")
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."
    except ValueError as e:
        return str(e)
def main():
    contacts = {}
    while True:
        command = input("Введіть команду (add, change, exit): ")
        if command == 'exit':
            break
        args = input("Введіть ім'я та телефон: ").split()
        if command == 'add':
            print(add_contact(args, contacts))
if __name__ == "__main__":
    main()
'''

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "This contact doesn't exist"

def show_all(args, contacts):
    name, phone = args
    return contacts[name]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(add_contact(args, contacts))
        elif command == "all":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()





if __name__ == '__main__':
    main()

