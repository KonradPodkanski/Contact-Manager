import manager
def main():
    filename = input("Enter file name: ").strip()
    cm = manager.ContactManager(f"{filename}")
    start_selection = int(input("Choose an option: \n(1) Load file \n(2) Create new file\n(3) Exit\n> "))

    if start_selection == 1:
        cm.load_file()
    if start_selection == 2:
        cm.create_new_file()
    if start_selection == 3:
        return
    while True:
        print(
            f"\n(1) - Add contact\n"
            f"(2) - Show contacts\n"
            f"(3) - Remove contact by email\n"
            f"(4) - Change phone number\n"
            f"(5) - Save changes\n"
            f"(6) - Exit\n"
        )
        print("Select option:")
        option = int(input(">"))
        if option == 1:
            name = input("Enter contact name: ")
            surname = input("Enter contact surname: ")
            phone_number = input("Enter contact phone number: ")
            mail = input("Enter contact mail: ")
            cm.add_contact(name, surname, phone_number, mail)

        if option == 2:
            cm.show_contact_list()

        if option == 3:
            cm.show_contact_list()
            print("-"*30)
            email = input("Enter contact email to remove: ")
            cm.remove_contact_by_email(email)
        if option == 4:
            cm.show_contact_list()
            print("-" * 30)
            phone_number = input("Enter contact phone number which you want to change: ")
            new_phone = input("Type new phone number: ").strip()
            cm.change_phone_number(phone_number, new_phone)
        if option == 5:
            cm.save_changes()
        if option == 6:
            print("See you later!")
            break


if __name__ == '__main__':
    main()