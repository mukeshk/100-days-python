from random import randint
from random import sample,choice

from sympy.physics.units import length

import art

print(art.logo)

players_goals_data = [
    {"player": "Cristiano Ronaldo", "goals": 890, "country": "Portugal"},
    {"player": "Lionel Messi", "goals": 827, "country": "Argentina"},
    {"player": "Pele", "goals": 767, "country": "Brazil"},
    {"player": "Romário", "goals": 753, "country": "Brazil"},
    {"player": "Ferenc Puskás", "goals": 746, "country": "Hungary"},
    {"player": "Gerd Müller", "goals": 735, "country": "Germany"},
    {"player": "Josef Bican", "goals": 805, "country": "Austria"},
    {"player": "Robert Lewandowski", "goals": 640, "country": "Poland"},
    {"player": "Zlatan Ibrahimović", "goals": 573, "country": "Sweden"},
    {"player": "Luis Suárez", "goals": 546, "country": "Uruguay"},
    {"player": "Eusébio", "goals": 541, "country": "Portugal"},
    {"player": "Hugo Sánchez", "goals": 512, "country": "Mexico"},
    {"player": "Alfredo Di Stéfano", "goals": 509, "country": "Argentina"},
    {"player": "Thierry Henry", "goals": 411, "country": "France"},
    {"player": "David Villa", "goals": 426, "country": "Spain"},
    {"player": "Wayne Rooney", "goals": 366, "country": "England"},
    {"player": "Samuel Eto'o", "goals": 426, "country": "Cameroon"},
    {"player": "Michael Owen", "goals": 262, "country": "England"},
    {"player": "Andriy Shevchenko", "goals": 379, "country": "Ukraine"},
    {"player": "George Weah", "goals": 193, "country": "Liberia"},
    {"player": "Harry Kane", "goals": 382, "country": "England"},
    {"player": "Kylian Mbappé", "goals": 302, "country": "France"},
    {"player": "Erling Haaland", "goals": 204, "country": "Norway"},
    {"player": "Neymar Jr.", "goals": 463, "country": "Brazil"},
    {"player": "Karim Benzema", "goals": 445, "country": "France"},
    {"player": "Antoine Griezmann", "goals": 290, "country": "France"},
    {"player": "Edinson Cavani", "goals": 436, "country": "Uruguay"},
    {"player": "Raúl", "goals": 404, "country": "Spain"},
    {"player": "Didier Drogba", "goals": 366, "country": "Ivory Coast"},
    {"player": "Carlos Tevez", "goals": 308, "country": "Argentina"},
    {"player": "Robin van Persie", "goals": 326, "country": "Netherlands"},
    {"player": "Alexis Sánchez", "goals": 220, "country": "Chile"},
    {"player": "Timo Werner", "goals": 160, "country": "Germany"},
    {"player": "Marco Reus", "goals": 170, "country": "Germany"},
    {"player": "Pierre-Emerick Aubameyang", "goals": 300, "country": "Gabon"},
    {"player": "Jamie Vardy", "goals": 180, "country": "England"},
    {"player": "Sergio Agüero", "goals": 427, "country": "Argentina"},
    {"player": "Mario Gómez", "goals": 270, "country": "Germany"},
    {"player": "Carlos Bacca", "goals": 200, "country": "Colombia"},
    {"player": "Wissam Ben Yedder", "goals": 200, "country": "France"},
    {"player": "Gonzalo Higuaín", "goals": 333, "country": "Argentina"},
    {"player": "Fernando Torres", "goals": 302, "country": "Spain"},
    {"player": "Ciro Immobile", "goals": 250, "country": "Italy"},
    {"player": "André-Pierre Gignac", "goals": 280, "country": "France"},
    {"player": "Gabriel Batistuta", "goals": 356, "country": "Argentina"},
    {"player": "Roberto Baggio", "goals": 291, "country": "Italy"},
    {"player": "Rivaldo", "goals": 338, "country": "Brazil"},
    {"player": "Claudio Pizarro", "goals": 336, "country": "Peru"},
    {"player": "Paolo Rossi", "goals": 134, "country": "Italy"}
]

print(len(players_goals_data))



player_2 = choice(players_goals_data)

continue_game = True
user_score = 0
while continue_game:
    player_1 = player_2
    player_2 = choice(players_goals_data)
    correct_answer = "A" if player_1['goals'] > player_2['goals'] else "B"
    print(f"Compare A: {player_1['player']} from {player_1['country']}")
    print(f"Against B: {player_2['player']} from {player_2['country']}")
    user_choice = input("Who has more goals? Type 'A' or 'B' ?: ").upper()
    continue_game = user_choice == correct_answer
    if continue_game:
        user_score += 1
        print(f"You are right! Current Score {user_score}")
    else:
        print(f"Sorry, that's wrong. Final Score {user_score}")

