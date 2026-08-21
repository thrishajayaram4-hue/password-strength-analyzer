password = input("Enter your password:")
print("Password entered successfully!")

length = len(password)
print("Password length:",length)
has_uppercase = any(char.isupper() for char in password)
print("Contains uppercase:",has_uppercase)
has_lowercase = any(char.islower() for char in password)
print("Contains lowercase:",has_lowercase)


