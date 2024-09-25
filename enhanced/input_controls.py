def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and validates it against a set of valid options.
    
    Args:
        prompt (str): The input prompt to display to the user.
        valid_options (set): A set of valid input options (e.g., {"A", "B", "C"}).
    
    Returns:
        str: The valid input provided by the user.
    """
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input
        print("Invalid input, please enter a valid option.")

# This section handles the invalid input logic. So if a particular input is not recognised by the program, it doesn't place any penalty on the user.