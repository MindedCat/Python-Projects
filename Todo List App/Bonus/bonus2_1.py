password = input("Enter password: ")

while password != "1234":
    print("Incorrect password. Please try again.")
    password = input("Enter password: ")

print("Password accepted.")