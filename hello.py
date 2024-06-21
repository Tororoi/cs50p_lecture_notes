# Ask the user for their name
# Remove whitespace from the name
# Capitalize the first letters of each word
name = input("Hello, what's your name? ").strip().title()

# Split the name into first and last name
first, last = name.split(" ")

# Say hello to the user
print(f"hello, {first}")
