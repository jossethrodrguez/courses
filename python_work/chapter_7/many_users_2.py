users = {}
def show_users():
    if users:
        print("\n-- USERS: --\n")
        for key, value in users.items():
            print(f"Username: {key} ")
            print(f"Fullname: {value['first'].title()} {value['last'].title()}\n")

active = True
while active:
    ask = input("\nDo you want add users? (Y/n): ")
    ask = (ask.strip()).lower()
    
    if (ask == 'y') or (ask == 'yes') or (ask == ''):
        username = (input("Type the username: ").lower()).strip()
        users[username] = {
            'first': (input("Type the first name: ").lower()).strip(),
            'last': (input("Type the last name: ").lower()).strip(),
            }

    else: 
        print("Bye!!!")
        active = False

show_users()
