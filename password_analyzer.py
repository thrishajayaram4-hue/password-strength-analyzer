password = input("Enter your password:")
print("Password entered successfully!")

length = len(password)
print("Password length:",length)
has_uppercase = any(char.isupper() for char in password)
print("Contains uppercase:",has_uppercase)
has_lowercase = any(char.islower() for char in password)
print("Contains lowercase:",has_lowercase)
has_number = any(char.isdigit() for char in password)
print("Contains number:",has_number)
has_special = any(not char.isalnum() for char in password)
print("Contains special character:",has_special)



