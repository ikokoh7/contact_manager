### Create the user database and register users
# Initialize an empty dictionary to store users' account details, login credentials, and contacts
user_database = {}  # Stores user details like name, email, and address
user_login_details = {}  # Stores user login credentials (username and password)
contacts = {}  # Stores user contacts

# Sign up
def create_new_user():
    # Handles user registration
    try:
        print("--- Create a new account ---\n")
        username = input("Enter your Username:\n>>  ").lower()
        password = make_password("new")
        # Ensures password meets the minimum length requirement
        if password == None:
            print("\nSorry, you need a Password to create your account\n")
            #print(f"Invalid Password count! {8 - len(password)} more characters left\n")
        else:
            print("\nPassword created successfully!\n")
            action = 0
            while action != "exit":
                if len(username) > 1:  # Validates that the username is not empty
                    user_login_details[username] = password  # Saves user credentials
                    print("\nCongratulations! Your account has been created successfully\n"
                        "You will be taken directly to your dashboard.")
                    return username
                print("You did not enter your Username")
                action = input("Enter your Username:\n(Enter 'exit' if you wish to exit the registration page)\n>>  ").lower()
    except Exception as e:
        print(e)
    return

def make_password(action):
    try:
        actions = ["new", "change"]
        if action in actions:
            password = input("Enter your Password:\n(Minimum character length should be 8) or '99' to exit\n>>  ")
            while action:
                if len(password) >= 8:
                    if password.isalpha():   
                        print("\nInvalid! Include atleast a Number and a Symbol (#,*,!,etc)\n")
                    elif password.isnumeric():
                        print("\nInvalid! Include atleast an Alphabet and a Symbol (#,*,!,etc)\n")
                    elif password.isalnum():
                        print("\nInvalid! Include atleast a Symbol (#,*,!,etc)\n")
                    else:
                        # Check for symbol characters and validate password
                        valid = {}
                        for char in password:
                            if char.isalpha():
                                valid["alpha"] = "pass"
                            elif char.isnumeric():
                                valid["numeric"] = "pass"
                            else:
                                valid["symbol"] = "pass"
                            # Check if password included all characters and return it
                            if len(valid) == 3:
                                valid.clear()
                                return password
                        if len(valid) == 1 and "symbol" in valid:
                            print("\nInvalid! Include atleast a Number and an Alphabet\n")
                        elif "numeric" in valid:
                            print("\nInvalid! Include atleast an Alphabet\n")
                        else:
                            print("\nInvalid! Include atleast a Number\n")
                elif password == "99":      # Exit the password page
                    print("\nPassword not created\n")
                    break
                else:
                    print("\nInvalid number of characters (Minimum character length should be 8)\n")
                # Check if function is called to change password and exit
                if action == "change":
                    return ""
                password = input("Enter Password again (Include all characters):\n>> ")
            else:
                print("Invalid choice! ")
    except Exception as e:
        print(e)
    return

from dashboard import view_dashboard, view_profile
from TODO import update_profile, task_manager, change_password

def user_session(user):
    # Manages the entire user session
    update_profile(user)  # Prompt for profile update on session start
    view = 0
    while view != 3:
        view = view_dashboard(user)
        if view == 1:
            task_manager()  # Opens task manager
        elif view == 2:
            profile = view_profile(user)
            if profile == "change":
                change_password(user)
            elif profile == "dashboard":
                continue
        elif view == 3:
            print("You have successfully logged out")
            break
        else:
            print("Invalid Choice!")