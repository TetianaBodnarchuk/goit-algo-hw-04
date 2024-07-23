def parse_input(user_input: str) -> str:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict) -> str:
    try:
        name, phone = args
        if name.isalpha() and phone.isdigit():
            contacts[name] = phone
            return 'Contact added.'
        else:
            return f'{name} is not word or {phone} is not number.'
    except ValueError:
        return 'Invalid number of arguments. Require name and one phone number.'

def change_contact(args: list, contacts: dict) -> str:
    try:
        name, phone = args
        if name.isalpha() and phone.isdigit():
            if name in contacts:
                contacts[name] = phone
                return 'Contact updated.'
            else:
                return 'Name not found.'
        else:
            return f'{name} is not word or {phone} is not number.'            
    except ValueError:
        print('Invalid number of arguments. Require name and one phone number.')

def show_phone(args: list, contacts: dict) -> str:
    try:
        name = args[0]
        if name in contacts and len:
            return contacts[name]
        else:
            return "This contact doesn't exist"
    except Exception:
        print('Invalid command.')

def show_all(contacts: dict) -> str:
    try:
        if not contacts:
            return f'The contacts list is empty.'
        else:
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
    except Exception:
        print('Invalid command.')

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
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
