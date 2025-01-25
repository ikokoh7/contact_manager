from user import contacts, user_database

def view_dashboard(user):
    # Displays the user's dashboard
    print(f"Welcome to your dashboard!\n")
    print("1. Contact List\n"
          "2. Profile\n"
          "3. Logout\n\n")
    action = input("What would you like to do? (Enter 1, 2, or 3):\n>> ")
    if action == "1":
        i = 1
        print(f"        Contact name                           Number            \n")
        # Displays all stored contacts
        for name, number in contacts.items():
            print(f"{i}. {name}                                      {number}")
            i += 1
        return 1
    elif action == "2":
        return 2
    elif action == "3":
        print("Do you want to Logout of your account?")
        return 3
    else:
        print("Invalid Choice!")

# View Profile
def view_profile(user):
    # Displays user profile details
    print(f"---- Profile ----\n"
          f"1. Username: {user}\n"
          f"2. E-mail: {user_database[user].get('E-mail')}\n"
          f"3. Name: {user_database[user].get('Name')}\n"
          f"4. Address: {user_database[user].get('Address', 'N/A')}\n"
          f"5. Phone number: {user_database[user].get('Phone number', 'N/A')}\n"
          f"6. Date of birth: {user_database[user].get('Date of birth', 'N/A')}\n\n")
    action = input("Enter 1 to change password or 99 to return to your dashboard.\n>> ")
    if action == "1":
        return "change"
    elif action == "99":
        return "dashboard"
    return True