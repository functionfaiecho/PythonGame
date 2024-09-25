def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and validates it against a set of valid options.
    
    Args:
        prompt (str): The input prompt to display to the user.
        valid_options (set): A set of valid input options (e.g., {"A", "B", "C"}).
    
    Returns:
        str: The valid input provided by the user.
    """
    # Infinite loop to continuously prompt the user for input until valid input is received.
    while True:
        # Takes user input, removes any surrounding spaces, and converts it to uppercase.
        user_input = input(prompt).strip().upper()
        # Checks if the user input is within the set of valid options.
        if user_input in valid_options:
            # If valid, return the input and exit the loop.
            return user_input
        # If invalid input is detected, it prints a message and re-prompts the user.
        print("Invalid input, please enter a valid option.")
