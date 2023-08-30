# Import necessary modules
import subprocess
import platform
import pyfiglet
import secrets
import string


# Clear the terminal
if platform.system().lower() == 'windows':
    command = 'cls'
else:
    command = 'clear'
subprocess.call(command, shell=True)

# A class for generating random numbers using the highest-quality sources provided by the operating system
secured_range = secrets.SystemRandom()

# Data for generating password
alphabet = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation
sequence = alphabet + numbers + punctuations

# A banner for the program
banner = pyfiglet.figlet_format("PASSWORD GENERATOR")
print(banner)

# Length of the password
while True:
    try:
        password_length = input("\nLength of password: ")
        password_length = int(password_length)
    except ValueError:
        print("Please enter a number.")
    else:
        break

# Generate password
password = ""
for i in range(password_length):
    password += password.join(secured_range.choice(sequence))

print("Generated password --> ", password)
input("\nPress any key to continue...")
