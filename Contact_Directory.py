aws_secret_access_key=tYOiy8z0/AQb+VzAi0auqNN8hV9B1Ny7K9AthvA8
agenda = {}
delimit = ""
def list_contacts():
    if agenda:
        for i in agenda:
            print ("+Name:", i)
            print ("+Phone number:", agenda[i]["numero"])
            print ("+Address:", agenda[i]["endereco"])
            print ("+Email:", agenda[i]["email"])
            print ("+------------------------------------------+")
    else:
        print("Schedule is empty")

#   -------------------------------------------------------------------------------

def search_contact(name):
    try:
        if name:
            print ("+Contact:", name, "founded")
            print ("+Name:", name)
            print ("+Phone number:", agenda[name]["numero"])
            print ("+Address:", agenda[name]["endereco"])
            print ("+E-mail:", agenda[name]["email"])
            print ("+-----------------------------------------------+")
    except:
        print("Contact not found!")

#   -------------------------------------------------------------------------------

def include_contacts(contato, telefone, email, endereco):
    try:
        agenda[contato] = {
            "numero":  telefone,
            "email":  email,
            "endereco":  endereco,
        }
        print("\n")
        print("Contact " + contato + " successfully added!")
        print("+Name:",contato)
        print("+Phone number:", agenda[contato]["numero"])
        print("+Address:", agenda[contato]["endereco"])
        print("+E-mail:", agenda[contato]["email"])
        print("+------------------------------------------+")
        save()

    except Exception as e:
        print("Error adding contact")
        print(e)


#   -------------------------------------------------------------------------------

def edit_contacts(contato, telefone, email, endereco):
    if contato in agenda:
        print("+Name:", contato)
        print("+Phone number:", agenda[contato]["numero"])
        print("+Address:", agenda[contato]["endereco"])
        print("+E-mail:", agenda[contato]["email"])
        print("+------------------------------------------+")
        print("+!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!+")
        agenda[contato] = {
            "numero": telefone,
            "email": email,
            "endereco": endereco,
        }
        save()
        print("Contact {} successfully edited!".format(contato))

    else:
        print("Contact nonexistent!")
    save()

#   -------------------------------------------------------------------------------

def exclude_contact(contato):
    try:
        agenda.pop(contato)
        save()
        print("Contact successfully deleted")
    except:
        print("Error deleting contact")

#   -------------------------------------------------------------------------------

def export_contacts(delimit, file_name):
    try:
        if delimit == "":
            delimit = ','
        with open(file_name, 'w') as file:
            for contato in agenda:
                num = agenda[contato]["numero"]
                end = agenda[contato]["endereco"]
                mail = agenda[contato]["email"]
                file.write("{}{}{}{}{}{}{}\n".format(contato, delimit, num, delimit, end, delimit,  mail))
        print("Exported!(Delimited by '{}')".format(delimit))
    except Exception as e:
        print("An error has occurred")
        print(e)

#   -------------------------------------------------------------------------------

def import_contact(file_name):
    try:
        with open(file_name) as file:
            line = file.readlines()
            for i in line:
                details = i.strip().split(',')
                nome = details[0]
                telefone = details[1]
                endereco = details[2]
                email = details[3]
                include_contacts(nome, telefone, endereco, email)
                save()
    except FileNotFoundError:
        print("File not Found")
    except Exception as e:
        print("An error an occurred")
        print(e)

#   -----------------------------------------------------------------------

def read_details():
    contato = input("Type contact: ")
    telefone = input("Type phone number: ")
    email = input("Type the email: ")
    endereco = input("Type the address:")
    return contato, telefone, email, endereco

#   -----------------------------------------------------------------------

def load():
    try:
        with open('database.csv') as file:
            line = file.readlines()
            for i in line:
                details = i.strip().split(',')
                nome = details[0]
                telefone = details[1]
                endereco = details[2]
                email = details[3]
                agenda[nome] = {
                    "numero": telefone,
                    "email": email,
                    "endereco": endereco,
                    }
        print("Number of contacts loaded: {}".format(len(agenda)))
    except FileNotFoundError:
        print("File not Found")
    except Exception as e:
        print("An error an occurred")
        print(e)

#   -----------------------------------------------------------------------

def save():
    export_contacts(delimit, 'database.csv')

#   -----------------------------------------------------------------------

def show_menu():
    print("+-----------------------------+")
    print("+ 1 - Show contacts           +")
    print("+ 2 - Search contacts         +")
    print("+ 3 - Add contacts            +")
    print("+ 4 - Edit contacts           +")
    print("+ 5 - Exclude contacts        +")
    print("+ 6 - Export contacts         +")
    print("+ 7 - Import contacts(.csv)   +")
    print("+ 0 - Exit                    +")
    print("+-----------------------------+")
load()
while True:
    print("\n")
    show_menu()
    resp = input("What do you want to do?\n")

    if resp == "1":
        list_contacts()
    elif resp == "2":
        name = input("Type contact name: ")
        search_contact(name)
    elif resp == "3":
        contato, telefone, email, endereco = read_details()
        include_contacts(contato, telefone, email, endereco)
    elif resp == "4":
        contato = input("Type contact name: ")
        telefone = input("Type phone number: ")
        email = input("Type the email: ")
        endereco = input("Type de address:")
        edit_contacts(contato, telefone, email, endereco)
    elif resp == "5":
        contato = input("Type contact name: ")
        exclude_contact(contato)
    elif resp == "6":
        delimit = input("Type contact name: ")
        name_file = input("Type the output file")
        export_contacts(delimit, name_file)
    elif resp == "7":
        file_name = input("Type file directory: ")
        import_contact(file_name)
    elif resp == "0":
        exit()
    else:
        print("Choice one of the options")
