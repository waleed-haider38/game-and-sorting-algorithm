import random
import string

def generate_password(length):
    # Sab characters combine karna
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly characters select karna
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


# User se input lena
length = int(input("Enter password length: "))

if length < 6:
    print("⚠️ Password length should be at least 6 for security.")
else:
    pwd = generate_password(length)
    print("🔐 Your Random Password is:", pwd)
