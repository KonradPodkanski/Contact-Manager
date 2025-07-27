class Contact:
    def __init__(self, name, surname, phone, email):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__email = email

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email

    def set_new_phone(self, new_phone):
        self.__phone = new_phone

    def __str__(self):
        return f"{self.__name}, {self.__surname}, {self.__phone}, {self.__email}"
    def __repr__(self):
        return self.__str__()

class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contact_list = []

    def load_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as contact_file:
                for line in contact_file:
                    contact = [part.strip() for part in line.split(",")]
                    if len(contact) == 4:
                        contact_obj = Contact(contact[0], contact[1], contact[2], contact[3])
                        self.contact_list.append(contact_obj)
                print("File loaded")
        except Exception as e:
            print(f"Error: {e}")
            return

    def create_new_file(self):
        try:
            with open(self.filename, "w", encoding="utf-8"):
                print(f"Created new file {self.filename}!\n")
                pass
        except Exception as e:
            print(f"Issue: {e}")

    def show_contact_list(self):
        for contact_obj in self.contact_list:
            print(contact_obj)

    def add_contact(self, name, surname, phone, email):
        contact = Contact(name, surname, phone, email)
        self.contact_list.append(contact)
        print("Added new contact!\n")

    def remove_contact_by_email(self, email):
        for contact_obj in self.contact_list:
            if contact_obj.get_email() == email.strip():
                self.contact_list.remove(contact_obj)
                print("Removed contact!\n")

    def change_phone_number(self, previous_phone, new_phone):
        for contact_obj in self.contact_list:
            if contact_obj.get_phone() == previous_phone.strip():
                contact_obj.set_new_phone(new_phone)
                print("Changed new phone number!\n")

    def save_changes(self):
        with open(self.filename, "w", encoding="utf-8") as contact_file:
            for contact in self.contact_list:
                contact_file.write(f"{contact.__str__()}\n")
            print("Saved file!\n")