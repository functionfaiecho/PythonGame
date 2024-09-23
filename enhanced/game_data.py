# Contains all my locations, travel costs and quiz questions and answers.

# Graph of locations with travel costs
locations = {
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

# Quiz questions for each location
questions = {
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
