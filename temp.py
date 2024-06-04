import random
import string

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Generate and print an 8-character random string
random_string = generate_random_string()
print(random_string)
