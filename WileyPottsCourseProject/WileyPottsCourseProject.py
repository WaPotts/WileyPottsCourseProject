from datetime import datetime

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def input_date_range():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            to_date = input("Enter to date (mm/dd/yyyy): ")
            from_date = datetime.strptime(from_date, "%m/%d/%Y").date()
            to_date = datetime.strptime(to_date, "%m/%d/%Y").date()
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def register_user():
    file_name = "users.txt"
    users = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                user_id, _, _ = line.strip().split("|")
                users[user_id] = True
    except FileNotFoundError:
        pass
    
    while True:
        user_id = input("Enter User ID (or type 'End' to stop): ")
        if user_id.lower() == "end":
            print("Returning to main menu...")
            return
        if user_id in users:
            print("User ID already exists. Choose another.")
            continue
        password = input("Enter Password: ")
        authorization = input("Enter Authorization (Admin/User): ")
        if authorization not in ["Admin", "User"]:
            print("Invalid authorization. Must be 'Admin' or 'User'.")
            continue
        with open(file_name, "a") as file:
            file.write(f"{user_id}|{password}|{authorization}\n")
        users[user_id] = True
        print("User registered successfully! Returning to menu...")
        return

def display_users():
    file_name = "users.txt"
    try:
        with open(file_name, "r") as file:
            print("\nRegistered Users:")
            for line in file:
                user_id, password, authorization = line.strip().split("|")
                print(f"User ID: {user_id}, Authorization: {authorization}")
    except FileNotFoundError:
        print("No users found.")

def login():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user_id, password, authorization = line.strip().split("|")
                users[user_id] = (password, authorization)
    except FileNotFoundError:
        print("No users registered. Please register a user first.")
        return None
    
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    if user_id not in users:
        print("Invalid User ID. Returning to menu.")
        return None
    if users[user_id][0] != password:
        print("Incorrect Password. Returning to menu.")
        return None
    return Login(user_id, password, users[user_id][1])

def process_authorized_actions(user):
    while True:
        if user.authorization == "Admin":
            print("Admin Access: You can enter and display data.")
            enter_employee_data()
        else:
            print("User Access: You can only display data.")
            process_and_display_records("employees.txt")
        break

def main():
    while True:
        print("\n1. Register Users\n2. Display Users\n3. Login\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            user = login()
            if user:
                process_authorized_actions(user)
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
