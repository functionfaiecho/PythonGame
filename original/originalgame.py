import datetime

class AdventureGame:
    def __init__(self):
        self.balance = 10.00
        self.location = "Changi Airport"
        self.visited_locations = set()
        self.locations = {
            "Changi Airport": {"Esplanade - Theatres on the Bay": 1.50, "Gardens by the Bay": 2.00, "Hawker Centre": 1.00, "Marina Bay Sands": 1.50},
            "Esplanade - Theatres on the Bay": {"Marina Bay Sands": 1.50, "Singapore Flyer": 1.00, "Chinatown": 1.00},
            "Gardens by the Bay": {"Sentosa Island": 2.50, "Little India": 1.50, "Hawker Centre": 1.00},
            "Hawker Centre": {"Jalan Sultan": 1.00, "Chinatown": 1.00, "Esplanade - Theatres on the Bay": 1.50},
            "Sentosa Island": {"Singapore Flyer": 1.00, "Gardens by the Bay": 2.00, "Marina Bay Floating Platform": 1.50},
            "Marina Bay Sands": {"Singapore Flyer": 1.00, "Gardens by the Bay": 2.00, "Hawker Centre": 1.00},
            "Singapore Flyer": {"Esplanade - Theatres on the Bay": 1.00, "Marina Bay Sands": 2.50, "Chinatown": 2.00},
            "Chinatown": {"Hawker Centre": 1.00, "Little India": 2.00, "Jalan Sultan": 2.00},
            "Jalan Sultan": {"Hawker Centre": 1.00, "Little India": 1.00, "Chinatown": 1.00},
            "Little India": {"Chinatown": 1.00, "Gardens by the Bay": 1.50, "Jalan Sultan": 1.00},
            "Marina Bay Floating Platform": {}  # Final destination, no further locations
        }
        self.questions = {
            "Esplanade - Theatres on the Bay": ("What fruit does the Esplanade resemble?", {"A": "Mango", "B": "Durian", "C": "Pineapple"}, "B"),
            "Gardens by the Bay": ("What is the name of the iconic structures that dominate the Gardens by the Bay?", {"A": "Flower Domes", "B": "Supertrees", "C": "Rain Trees"}, "B"),
            "Hawker Centre": ("You're served a dish that includes coconut rice, fried anchovies, and sambal. What is it?", {"A": "Chicken Rice", "B": "Nasi Lemak", "C": "Laksa"}, "B"),
            "Sentosa Island": ("Guess the year Sentosa was developed into a resort.", {"A": "1960", "B": "1972", "C": "1985"}, "B"),
            "Marina Bay Sands": ("Which famous architect designed Marina Bay Sands?", {"A": "Norman Foster", "B": "Moshe Safdie", "C": "Zaha Hadid"}, "B"),
            "Singapore Flyer": ("How tall is the Singapore Flyer?", {"A": "165m", "B": "150m", "C": "175m"}, "A"),
            "Chinatown": ("Which traditional Chinese festival is most prominently celebrated in Chinatown?", {"A": "Qingming Festival", "B": "Dragon Boat Festival", "C": "Chinese New Year"}, "C"),
            "Jalan Sultan": ("Jalan Sultan is famous for which historic mosque?", {"A": "Masjid Sultan", "B": "Masjid Alkaff", "C": "Masjid Malabar"}, "A"),
            "Little India": ("During which festival do devotees carry decorated 'kavadis' as a sign of devotion?", {"A": "Diwali", "B": "Thaipusam", "C": "Pongal"}, "B"),
            "Marina Bay Floating Platform": ("The Marina Bay Floating Platform was originally built for which event?", {"A": "National Day Parade", "B": "F1 Grand Prix", "C": "New Year's Eve"}, "A"),
        }

    def travel(self, destination):
        cost = self.locations[self.location].get(destination, 0)  # Get the cost, default to 0 if not found
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
            print(question)
            for option, answer in options.items():
                print(f"{option}: {answer}")
            user_answer = input("Your answer: ").strip().upper()
            if user_answer == correct_answer:
                self.balance += 1.00
                print(f"Correct! You earned $1.00. Your new balance is ${self.balance:.2f}.")
            else:
                self.balance -= 1.00
                print(f"That's not correct. You lost $1.00. Your new balance is ${self.balance:.2f}.")

    def play(self):
        print("Welcome to Singapore! You start your journey at Changi Airport with $10.00.")
        while True:
            print(f"\nYou are currently at {self.location}. Where would you like to go?")
            
            # Filter out visited locations from the available destinations
            available_destinations = {k: v for k, v in self.locations[self.location].items() if k not in self.visited_locations}
            
            # If 6 or more locations have been visited, add Marina Bay Floating Platform as an option
            if len(self.visited_locations) >= 6 and "Marina Bay Floating Platform" not in self.visited_locations:
                available_destinations["Marina Bay Floating Platform"] = self.locations[self.location].get("Marina Bay Floating Platform", 1.50)
            
            # If no other locations available and no money left to reach the final destination, game over
            if not available_destinations or (available_destinations and self.balance < min(available_destinations.values())):
                print("\nYou've run out of money! Game over.")
                break

            # List the possible destinations with numbers
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
