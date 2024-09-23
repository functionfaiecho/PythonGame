def dfs_collect_answers(location, locations, questions, visited):
    """
    DFS traversal to visit all locations and collect/display correct answers
    for each location's quiz question.
    
    Args:
        location (str): The starting location for DFS.
        locations (dict): The graph of locations and their travel costs.
        questions (dict): The questions and answers for each location.
        visited (set): A set to keep track of visited locations.
    """
    if location in visited:
        return
    visited.add(location)

    # If the location has a quiz question, show the correct answer
    if location in questions:
        question, options, correct_answer = questions[location]
        print(f"{location} - {question}")
        print(f"The correct answer is: {correct_answer}\n")
    
    # Recursively visit all connected locations
    for next_location in locations[location]:
        dfs_collect_answers(next_location, locations, questions, visited)


def activate_cheat(location, locations, questions):
    """
    Function to activate cheat mode and display the correct answers using DFS.
    
    Args:
        location (str): The current location of the player.
        locations (dict): The graph of locations.
        questions (dict): The questions and answers for each location.
    """
    print("\nCheat mode activated! Showing correct answers for all quiz questions:")
    visited = set()  # To keep track of visited locations
    dfs_collect_answers(location, locations, questions, visited)
    print("Cheat mode traversal completed!\n")
