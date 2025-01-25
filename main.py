from login import login_page_message, get_login_details
from user import create_new_user, user_session


login_page_message()
user = get_login_details()
if user == "new user":
    user = create_new_user()
elif user == False:
    print("Goodbye! Wish to see you soon")
else:
    print("Login Successful")
while True:
    status = user_session(user)
    if status == "logout":
        break