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
score = 0
if length >= 8:
  score += 1
if has_lowercase:
  score += 1
if has_uppercase:
  score += 1
if has_number:
  score += 1
if has_special:
  score += 1
if score <=2:
  print("Password strength: Weak")
elif score <= 4:
  print("Password strength: Medium")
else:
  print("Password strength: Strong")
print("\nSecurity checks:")
print("Length 8+:",length>=8)
print("Lowercase:",has_lowercase)
print("uppercase:",has_uppercase)
print("Number:",has_number)
print("Special character:",has_special)
if score < 5:
  print("Suggestion: Use at least 8 characters with uppercase,lowercase,a number,and a special character")
else:
  print("Your password meets all the basic strength requirements")
has_unique_chars = len(set(password)) == len(password)
print("Unique characters:",has_unique_chars)





