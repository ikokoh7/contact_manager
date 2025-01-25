### Create the user database and register users
# Initialize an empty dictionary to store users' account details, login credentials, and contacts
user_database = {}  # Stores user details like name, email, and address
user_login_details = {}  # Stores user login credentials (username and password)
contacts = {}  # Stores user contacts

# Sign up
def create_new_user():
    # Handles user registration
    print("--- Create a new account ---\n")
    username = input("Enter your Username:\n>>  ").lower()
    password = input("Enter your Password:\n(Minimum character length should be 8)\n>>  ")
    # Ensures password meets the minimum length requirement
    while len(password) < 8:
        print(f"Invalid Password count! {8 - len(password)} more characters left\n")
        password = input("Enter a Password (Minimum length: 8 and Include all characters) or type 'stop' to exit:\n>> ")
    action = 0
    while action != "exit":
        if len(username) > 1:  # Validates that the username is not empty
            user_login_details[username] = password  # Saves user credentials
            print("Congratulations! Your account has been created successfully\n"
                  "You will be taken directly to your dashboard.")
            break
        print("You did not enter your Username")
        action = input("Enter your Username:\n(Enter 'exit' if you wish to exit the registration page)\n>>  ").lower()
    return username

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