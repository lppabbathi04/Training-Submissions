import random
import string  # gives us ready-made lists of letters, digits, and punctuation

# Step 1: Ask the user for password length
length = int(input("Enter the length of the password: "))

# Step 2: Create character pool (letters + digits + punctuation)
characters = string.ascii_letters + string.digits + string.punctuation
# ascii_letters = A-Z and a-z
# digits = 0-9
# punctuation = symbols like !@#$%^&*

# Step 3: Randomly choose characters and build password
password = ''.join(random.choice(characters) for i in range(length))

# Step 4: Print the password
print("Generated Password:", password)
