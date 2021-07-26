# Function that generates a random password based on the provided length.
# Uses the random module, and the string module.
# The default lenght is 8.
def password_generator(length=8):
    import random
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))