def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact with name '{name}' already exists. Please choose another name."
    else:
        contacts[name] = phone
        return "Contact added."
    
def change_contact(args,contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"New contact number {phone} is updated."
    else:
        return f"No name {name} is found in contacts."
    
def show_phone(args,contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for '{name}' is {contacts[name]}"
    else:
        return f"No name '{name}' is found in contacts."
    

def show_all(contacts):
    if contacts:
        return contacts
    else:
        return "No contacts."
    
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


