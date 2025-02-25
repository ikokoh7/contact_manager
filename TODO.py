from user import user_database, user_login_details, contacts
from user import make_password

# Password change functionality
def change_password(user):
    # Allows users to change their password
    try:
        password = user_login_details[user]
        no_of_tries = 1
        print("---- Change Password ----")
        while no_of_tries <= 3:  # Gives the user 3 attempts to change their password
            Old_password = input("\nCurrent Password:\n>> ")
            if Old_password == password:  # Validates the old password
                print("\n**Enter new Password**\n")
                New_password = make_password("change")
                if (len(New_password) > 8):
                    print("\n**Confirm new Password**\n")
                    New_password_again = make_password("change")
                    if (New_password == New_password_again):
                            user_login_details[user] = New_password
                            print("Password updated successfully!")
                            return True
                    else:
                        print("Invalid! Passwords do not match")
            print("Invalid Password!\n"
                f"You have {3 - no_of_tries} tries more to change the password")
            no_of_tries += 1
        print("\nUnfortunately, you have used all your tries to change the password.")
    except Exception as e:
        print(e)
    return False

# Update Profile
def update_profile(user):
    # Allows users to update their profile details
    print("1. Update Profile\n"
          "99. Exit\n")
    try:
        action = input("Enter 1 to change profile details or 99 to exit:\n>>> ")
        if action == "1":
            user_name = user
            first_name = input('Enter your First Name:\n>> ').rstrip()
            last_name = input("Enter your Last Name:\n>> ")
            email = input("Enter your E-mail:\n>> ")
            address = input("Enter your Address:\n>> ")
            phone = input("Enter your Phone number:\n>> ")
            date_of_birth = input("Enter your Date of birth:\n>> ")
            user_info = {
                "First Name": first_name,
                "Last Name": last_name,
                "E-mail": email,
                "Address": address,
                "Phone number": phone,
                "Date of birth": date_of_birth,
            }
            user_database[user_name] = user_info
            print("Profile updated Successfully")
            return True
        elif action == "99":
            return False
        else:
            print("Invalid Choice!")
    except Exception as e:
        print(e)
    return False

# Task Manager
def task_manager(user):
    # Allows users to manage their contacts
    print("Would you like to:\n"
          "1. Add a new contact\n"
          "2. View your contact list\n"
          "3. Delete contact\n"
          "4. Update contact list\n"
          "99. Exit\n")
    try:
        contacts[user] = {}
        action = 0
        while action != "99":
            action = input("Enter your choice of tasks (1, 2, 3, 4) or 99 to exit:\n>> ")
            if action == "1":
                name = input("Enter Contact Name:\n>> ")
                number = input("Enter Contact Number:\n>> ")
                # Adds a new contact
                contact_info = {
                name: [number]
                }
                contacts[user] = contact_info
            elif action == "2":
                i = 1
                print(f"        Contact name                           Number            \n")
                for name, number in contacts[user].items():
                    print(f"{i}. {name}                                      {number[0]}")
                    i += 1
            elif action == "3":
                delete_contact = input("Enter Contact name to be deleted:\n>> ")
                contacts[user].pop(delete_contact, None)  # Deletes a contact
            elif action == "4":
                update_name = input("Enter Contact Name to be updated:\n>> ")
                update_number = input("Enter Contact Number:\n>> ")
                if update_name in contacts[user]:
                    contacts[user][update_name][0] = update_number # Updates a contact number
                else:
                    print("Would you like to add the contact to your list? Enter 1 to continue")
                    option = input(">> ")
                    if option == "1":
                        contacts[user][update_name][0] = update_number
                    else:
                        print("Invalid Choice!")
            elif action == "99":
                break
            else:
                print("Invalid Choice!")
    except Exception as e:
        print(e)