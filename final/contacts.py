import random


savefile_name = "contacts.csv"
commands_file = "commands.txt"


def about():
    """ prints information about the developer """
    print('Contacts App. Developed by Chandra Sundaram for CSE107 2019')


def info(contacts):
    """ Print number of contacts, print number of companies,
        print number of contacts per company """
    if not contacts:
        print('Currently no contacts in contact list')
    else:
        companies = {}
        for name in contacts:
            person = contacts[name]
            maybe_company = companies.get(person['company'])
            if maybe_company:
                old_count = companies[person['company']]
                companies[person['company']] = old_count + 1
            else:
                companies[person['company']] = 1
        print("Number of contacts: ", len(contacts))
        print("Number of companies: ", len(companies))
        print("Contacts per company: ")
        for company in companies:
            head_count = companies[company]
            print("\t {} with head count {}".format(company, head_count))


def list(contacts):
    """ prints all contacts in dictionary """
    print('Name:       Phone       Company       Email')
    print('-----------------------------------------------')

    if not contacts:
        print('EMPTY')
    else:
        for name in contacts:
            person = contacts[name]
            print("{}:       {}  {}  {}".format(name,
                                                person['phone'],
                                                person['company'],
                                                person['email']))


def remove(contacts):
    """ takes in contact list and element to be removed from list and removes
    each item individually from list """
    if not contacts:
        print('Currently no contacts in contact list')
    else:
        person = input('Who would you like to remove? ')
        if person in contacts:
            del contacts[person]
            print(person + ' had been removed for your contacts')
        else:
            print('contact does not exist')

    return contacts


def note(cont):
    """ allows user to view or edit note for given contact, person """
    if not cont:
        print('Currently no contacts in contact list')
    else:
        com = input('would you like to edit or view your notes?: ')
        if com == 'view':
            person = input('Who\'s note would you like to see? ')
            print(cont[person[-1]])
        elif com == 'edit':
            person = input('Who\'s note would you like to edit? ')
            note = input('write your new note: ')
            cont[person].append(note)
    return cont


def save(contacts):
    """ additional functions """
    with open(savefile_name, 'w', encoding='utf-8') as savefile:
        for name in contacts:
            person = contacts[name]
            savefile.write("{}, {}, {}, {}, {}\n".format(person['name'],
                                                         person['phone'],
                                                         person['company'],
                                                         person['email'],
                                                         person.get('note')))

def load(contacts):
    """ additional functions """
    with open(savefile_name, 'r', encoding='utf-8') as readfile:
        for line in readfile:
            # Chandra, 5551234, Microsoft, cha@microsoft, Chandra
            (name, phone, company, email, maybe_note) = line.split(", ")
            if maybe_note.strip() == "None":
                note = None
            else:
                note = maybe_note
            loaded_contact = make_contact(name, phone, company, email, note)
            contacts[name] = loaded_contact
    return contacts


def commands(contacts):
    """ additional functions """
    add_prefix = "add "
    remove_prefix = "remove "
    # doesn't make sense
    # name_prefix = "name: "
    phone_prefix = "phone: "
    company_prefix = "company: "
    email_prefix = "email: "
    note_prefix = "note: "
    with open(commands_file, 'r', encoding='utf-8') as readfile:
        current_person = None
        for line in readfile:
            stripped = line.strip()
            if stripped[0:4] == add_prefix:
                name = stripped.split(add_prefix)[1]
                if current_person:
                    contacts[current_person['name']] = current_person
                current_person = {"name": name}
            elif stripped[0:7] == remove_prefix:
                if current_person:
                    contacts[current_person['name']] = current_person
                current_person = None
                name = stripped.split(remove_prefix)[1]
                if contacts.get(name):
                    del contacts[name]
            # name field-command doesn't make sense
            # elif stripped[0:6] == name_prefix:
            #     if current_person:
            #         pass
            #     elif:
            #         raise Exception('Tried to parse name before add command')
            elif stripped[0:7] == phone_prefix:
                if current_person:
                    phone = stripped.split(phone_prefix)[1]
                    current_person['phone'] = phone
                else:
                    raise Exception('Tried to parse phone before add command')
            elif stripped[0:9] == company_prefix:
                if current_person:
                    company = stripped.split(company_prefix)[1]
                    current_person['company'] = company
                else:
                    raise Exception('Tried to parse company\
                     before add command')

            elif stripped[0:7] == email_prefix:
                if current_person:
                    email = stripped.split(email_prefix)[1]
                    current_person['email'] = email

                else:
                    raise Exception('Tried to parse email before add command')

            elif stripped[0:6] == note_prefix:
                if current_person:
                    note = stripped.split(note_prefix)[1]
                    current_person['note'] = note
                else:
                    raise Exception('Tried to parse note before add command')
        if current_person:
            contacts[current_person['name']] = current_person


def make_contact(name, phone, company, email, note=None):
    """ additional functions """
    return {"name": name,
            "phone": phone,
            "company": company,
            "email": email,
            "note": note}


def add_contact(contacts):
    """ takes in dictionary for contacts. Requests information about contact,
    inputs into dictionary, returns dictionary with new contact """
    name = input('Enter new contact\'s name: ')
    phone = input('Enter ' + name + '\'s phone number: ')
    company = input('Which company does ' + name + ' work for: ')
    email = input('Enter ' + name + '\'s email: ')
    note = input('would you like to make a note for this contact? ')

    if note == 'no':
        contacts[name] = make_contact(name, phone, company, email)
    else:
        note = input('note: ')
        contacts[name] = make_contact(name, phone, company, email, note)
    return contacts


def main():
    print('Welcome to the Contact application')
    contacts = {}
    command = input('Please enter a command: ')

    while(command != 'exit'):
        if command == 'about':
            about()
        elif command == 'info':
            info(contacts)
        elif command == 'list':
            list(contacts)
        elif command == 'remove':
            remove(contacts)
        elif command == 'note':
            note(contacts)
        elif command == 'add':
            add_contact(contacts)
        elif command == 'load':
            load(contacts)
        elif command == 'save':
            save(contacts)
        elif command == 'commands':
            commands(contacts)
        command = input('Please enter a command: ')
    print('GoodBye')


if __name__ == "__main__":
    main()
    # chris_contact = {"name": "Chris",
    #                  "phone": "5551233",
    #                  "company": "Microsoft",
    #                  "email": "chris@microsoft",
    #                  "note": None}
    # chandra_contact = {"name": "Chandra",
    #                  "phone": "5551234",
    #                  "company": "Microsoft",
    #                  "email": "cha@microsoft",
    #                  "note": None}
    # mike_contact = {"name": "Mike",
    #                  "phone": "phone",
    #                  "company": "Adbeware",
    #                  "email": "mike@adbeware",
    #                  "note": None}
    #
    # contact_db = {'Chris': chris_contact,
    #               'Chandra': chandra_contact,
    #               'Mike': mike_contact
    #              }
    # info(contact_db)
    # print("\n\n")
    # list(contact_db)
    # # remove(contact_db)
    # print(contact_db)
    # # note(contact_db)
    # # print(contact_db)
    # save(contact_db)
    # new_contact_db = load(contact_db)
    # print(new_contact_db)
    # commands(contact_db)
    # print(contact_db)
