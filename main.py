python
def display_welcome_message() -> None:
    """
    Function to display a welcome message to the user.
    Outputs a string "Hello, World!" to the console.
    """
    print("Hello, World!")

def program_entry_point() -> None:
    """
    The main function that serves as the entry point to the program.
    Calls the function to display the welcome message.
    """
    display_welcome_message()

if __name__ == "__main__":
    program_entry_point()