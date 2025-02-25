from user import user_login_details

# Login Page
def login_page_message():
    # Displays login page options
    print("---- Welcome back! ---\n")
    print("Sign In To Your Account\n\n"
          "New user? Register here")

def get_login_details():
    # Handles user login
    try:
        action = 0
        while action != "99":
            action = input("Enter '1' if you have an account or '2' to create a new account or 'any' to exit the page:\n>> ")
            if action == "1":
                user_name = input("Username:\n>> ")
                password = input("Password:\n>> ")
                # Checks if username exists in the user database
                if user_name in user_login_details:
                    if password == user_login_details.get(user_name):  # Compares entered password with stored password
                        return user_name
                    else:
                        while True:
                            print("Wrong Password! Enter correct password or enter 99 to exit")
                            password = input("Password:\n>> ")
                            if password == "99":
                                break
                        return False
                else:
                    print("Invalid Username or Password!")
            elif action == "2":
                return "new user"  # Redirects to account creation
            else:
                print("Invalid Choice!")
    except Exception as e:
        print(e)