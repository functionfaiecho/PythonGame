import datetime
from utils import dijkstra_algorithm  # Import Dijkstra logic
from game_data import locations, questions  # Import locations and questions
from input_controls import get_valid_input  # Import the input validation utility

class AdventureGame:
    def __init__(self):
        self.balance = 10.00
        self.location = "Changi Airport"
        self.visited_locations = set()

        # Use imported locations and questions
        self.locations = locations
        self.questions = questions
        self.cheat_activated = False

    def travel(self, destination):
        cost = self.locations[self.location].get(destination, 0)
        if self.balance >= cost:
            self.balance -= cost
            self.visited_locations.add(self.location)
            self.location = destination
            print(f"You've arrived at {destination}. Your remaining balance is ${self.balance:.2f}.")
            if destination != "Marina Bay Floating Platform":
                self.ask_question(destination)
        else:
            print("You don't have enough money to travel there.")

    def ask_question(self, location):
        if location in self.questions:
            question, options, correct_answer = self.questions[location]

            # Show the correct answer along with the question if cheat mode is activated
            if self.cheat_activated:
                print(f"{question} (CHEAT MODE: ANSWER {correct_answer})")
            else:
                print(question)

            # Display the options for the question
            for option, answer in options.items():
                print(f"{option}: {answer}")

            # Regardless of cheat mode, get user input and validate
            user_answer = get_valid_input("Your answer: ", set(options.keys()))
            
            # Provide feedback based on user's answer
            if user_answer == correct_answer:
                self.balance += 1.00
                print(f"Correct! You earned $1.00. Your new balance is ${self.balance:.2f}.")
            else:
                print(f"That's not correct. No penalty. Your balance remains ${self.balance:.2f}.")

    def activate_cheat(self):
        question = "When did Singapore gain its independence?"
        options = {"A": "1959", "B": "1965", "C": "1971"}
        correct_answer = "B"

        print(question)
        for option, answer in options.items():
            print(f"{option}: {answer}")

        # Validate input for the cheat question
        user_answer = get_valid_input("Your answer to activate the cheat: ", set(options.keys()))

        if user_answer == correct_answer:
            print("Correct! Cheat mode activated.")
            self.cheat_activated = True
            # Use Dijkstra's algorithm to show the easiest way to reach the final destination
            self.easy_way_to_marina_bay()
        else:
            print("Incorrect. Cheat mode not activated.")

    def easy_way_to_marina_bay(self):
        if not self.cheat_activated:
            return

        print("\nCalculating the easiest way to reach Marina Bay Floating Platform using Dijkstra's Algorithm...")

        # Call Dijkstra's algorithm from the utility file
        best_path, min_cost = dijkstra_algorithm(self.locations, self.location, "Marina Bay Floating Platform", 6)

        if best_path:
            print("Easiest path found!")
            print(" -> ".join(best_path))
            print(f"Total cost: ${min_cost:.2f}")
        else:
            print("No valid path found with at least 6 locations visited.")

    def play(self):
        print("Welcome to Singapore! You start your journey at Changi Airport with $10.00.")
        
        # Ask the initial cheat question at the beginning of the game
        self.activate_cheat()

        while True:
            print(f"\nYou are currently at {self.location}. Where would you like to go?")

            available_destinations = {k: v for k, v in self.locations[self.location].items() if k not in self.visited_locations}

            if len(self.visited_locations) >= 6 and "Marina Bay Floating Platform" not in self.visited_locations:
                available_destinations["Marina Bay Floating Platform"] = self.locations[self.location].get("Marina Bay Floating Platform", 1.50)

            if not available_destinations or (available_destinations and self.balance < min(available_destinations.values())):
                print("\nYou've run out of money! Game over.")
                break

            destinations = list(available_destinations.items())
            for index, (destination, cost) in enumerate(destinations, start=1):
                print(f"{index}. {destination} (Cost: ${cost:.2f})")

            try:
                choice = int(input("Enter the number of your destination: ").strip())
                if 1 <= choice <= len(destinations):
                    destination = destinations[choice - 1][0]
                    self.travel(destination)
                else:
                    print("Invalid choice. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            if self.location == "Marina Bay Floating Platform":
                current_year = datetime.datetime.now().year
                singapore_age = current_year - 1965
                suffix = "th"
                if singapore_age % 10 == 1 and singapore_age != 11:
                    suffix = "st"
                elif singapore_age % 10 == 2 and singapore_age != 12:
                    suffix = "nd"
                elif singapore_age % 10 == 3 and singapore_age != 13:
                    suffix = "rd"

                print(f"\nWelcome to the Floating Platform. This year, Singapore celebrates its {singapore_age}{suffix} birthday.")
                print("People of all races, beliefs, and walks of life live together in harmony on this tiny red dot, the Lion City, the place that we call our home.")
                print("If you haven't yet visited Singapore, please take this as my personal invitation to come and visit. If you have visited before, we look forward to welcoming you back to Singapore again soon. If you are a Singaporean or call Singapore home, I hope that this game has brought a little slice of home to you - no matter where you may be in the world.")
                print("This game was created by a very homesick 28 year-old.")
                print(f"You've reached the final destination with ${self.balance:.2f} left. Congratulations!")
                break

if __name__ == "__main__":
    game = AdventureGame()
    game.play()
