import datetime
from utils import dijkstra_algorithm  # Import Dijkstra's algorithm for pathfinding
from game_data import locations, questions  # Import predefined locations and quiz questions
from input_controls import get_valid_input  # Import the utility to validate user inputs

class AdventureGame:
    def __init__(self):
        self.balance = 10.00  # Start the player with a balance of $10.00
        self.location = "Changi Airport"  # The starting location for the player
        self.visited_locations = set()  # Use a set to track visited locations

        # Load the locations and quiz questions from the external game_data module
        self.locations = locations
        self.questions = questions
        self.cheat_activated = False  # Cheat mode starts as deactivated

    def travel(self, destination):
        # Check the travel cost from the current location to the chosen destination
        cost = self.locations[self.location].get(destination, 0)
        
        # If the player has enough balance, travel to the destination
        if self.balance >= cost:
            self.balance -= cost  # Deduct the cost from the player's balance
            self.visited_locations.add(self.location)  # Mark the current location as visited
            self.location = destination  # Update the current location
            print(f"You've arrived at {destination}. Your remaining balance is ${self.balance:.2f}.")
            
            # If the destination is not the final destination, ask a quiz question
            if destination != "Marina Bay Floating Platform":
                self.ask_question(destination)
        else:
            # Inform the player if they don't have enough money to travel
            print("You don't have enough money to travel there.")

    def ask_question(self, location):
        # Check if the location has an associated quiz question
        if location in self.questions:
            question, options, correct_answer = self.questions[location]

            # If cheat mode is on, show the correct answer along with the question
            if self.cheat_activated:
                print(f"{question} (CHEAT MODE: ANSWER {correct_answer})")
            else:
                # Otherwise, just show the question and options
                print(question)

            # Display the available answer options (A, B, C)
            for option, answer in options.items():
                print(f"{option}: {answer}")

            # Always prompt the user to input their answer, even in cheat mode
            user_answer = get_valid_input("Your answer: ", set(options.keys()))
            
            # Check if the player's answer matches the correct answer
            if user_answer == correct_answer:
                self.balance += 1.00  # Reward the player $1.00 for a correct answer
                print(f"Correct! You earned $1.00. Your new balance is ${self.balance:.2f}.")
            else:
                # If the answer is wrong, no penalty is applied (as per your current rules)
                print(f"That's not correct. No penalty. Your balance remains ${self.balance:.2f}.")

    def activate_cheat(self):
        # A simple quiz to activate cheat mode
        question = "When did Singapore gain its independence?"
        options = {"A": "1959", "B": "1965", "C": "1971"}
        correct_answer = "B"

        # Present the cheat mode activation question
        print(question)
        for option, answer in options.items():
            print(f"{option}: {answer}")

        # Validate the player's input for the cheat activation question
        user_answer = get_valid_input("Your answer to activate the cheat: ", set(options.keys()))

        # If the player answers correctly, activate cheat mode
        if user_answer == correct_answer:
            print("Correct! Cheat mode activated.")
            self.cheat_activated = True  # Mark cheat mode as activated
            # Call Dijkstra's algorithm to show the easiest path to the final destination
            self.easy_way_to_marina_bay()
        else:
            # If the answer is wrong, do not activate cheat mode
            print("Incorrect. Cheat mode not activated.")

    def easy_way_to_marina_bay(self):
        # Skip if cheat mode is not activated
        if not self.cheat_activated:
            return

        print("\nCalculating the easiest way to reach Marina Bay Floating Platform using Dijkstra's Algorithm...")

        # Use Dijkstra's algorithm to find the best path
        best_path, min_cost = dijkstra_algorithm(self.locations, self.location, "Marina Bay Floating Platform", 6)

        # Output the path and the cost, or report no valid path
        if best_path:
            print("Easiest path found!")
            print(" -> ".join(best_path))  # Display the path taken
            print(f"Total cost: ${min_cost:.2f}")
        else:
            # Notify if no valid path was found with at least 6 locations visited
            print("No valid path found with at least 6 locations visited.")

    def play(self):
        # Starting message for the player
        print("Welcome to Singapore! You start your journey at Changi Airport with $10.00.")
        
        # Ask the initial cheat question at the beginning of the game
        self.activate_cheat()

        while True:
            print(f"\nYou are currently at {self.location}. Where would you like to go?")

            # Get all available destinations excluding already visited locations
            available_destinations = {k: v for k, v in self.locations[self.location].items() if k not in self.visited_locations}

            # If the player has visited 6 or more locations, allow travel to the final destination
            if len(self.visited_locations) >= 6 and "Marina Bay Floating Platform" not in self.visited_locations:
                available_destinations["Marina Bay Floating Platform"] = self.locations[self.location].get("Marina Bay Floating Platform", 1.50)

            # If no destinations are left or the player can't afford any, end the game
            if not available_destinations or (available_destinations and self.balance < min(available_destinations.values())):
                print("\nYou've run out of money! Game over.")
                break

            # Show all possible destinations with their travel costs
            destinations = list(available_destinations.items())
            for index, (destination, cost) in enumerate(destinations, start=1):
                print(f"{index}. {destination} (Cost: ${cost:.2f})")

            try:
                # Ask the player to choose a destination by number
                choice = int(input("Enter the number of your destination: ").strip())
                if 1 <= choice <= len(destinations):
                    destination = destinations[choice - 1][0]
                    self.travel(destination)  # Travel to the selected destination
                else:
                    print("Invalid choice. Please choose a valid number.")
            except ValueError:
                # Handle invalid input (not a number)
                print("Invalid input. Please enter a number.")

            # Check if the player has reached the final destination
            if self.location == "Marina Bay Floating Platform":
                current_year = datetime.datetime.now().year
                singapore_age = current_year - 1965  # Calculate Singapore's age
                suffix = "th"  # Default suffix for the age
                if singapore_age % 10 == 1 and singapore_age != 11:
                    suffix = "st"
                elif singapore_age % 10 == 2 and singapore_age != 12:
                    suffix = "nd"
                elif singapore_age % 10 == 3 and singapore_age != 13:
                    suffix = "rd"

                # Display the final message when reaching the Floating Platform
                print(f"\nWelcome to the Floating Platform. This year, Singapore celebrates its {singapore_age}{suffix} birthday.")
                print("People of all races, beliefs, and walks of life live together in harmony on this tiny red dot, the Lion City, the place that we call our home.")
                print("If you haven't yet visited Singapore, please take this as my personal invitation to come and visit. If you have visited before, we look forward to welcoming you back to Singapore again soon.")
                print("This game was created by a very homesick 28 year-old.")
                print(f"You've reached the final destination with ${self.balance:.2f} left. Congratulations!")
                break

if __name__ == "__main__":
    # Initialise and start the game
    game = AdventureGame()
    game.play()
