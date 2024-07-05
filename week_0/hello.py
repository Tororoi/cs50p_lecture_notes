# Say hello to the world and the user
def main():
    # Say hello to the world
    hello()
    # Ask the user for their name
    name = input("Hello, what's your name? ")
    # Say hello to the user
    hello(name)

# Say hello
def hello(to="world"):
    # Remove whitespace from the name
    # Capitalize the first letters of each word
    # Split the input into a list of words
    # Get the first word from the list
    first = to.strip().title().split(" ")[0]
    print(f"Hello, {first}!")

main()
