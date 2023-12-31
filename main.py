import json


def calculate_streak(all_games, length, username):
    probabilities = []
    for start_game in range(len(all_games) - length + 1):
        probability = 1
        for i in range(length):
            game = all_games[start_game + i]
            for color in ['white', 'black']:
                if game[color]['username'] == username:
                    probability *= game[color]['winning_chance']
                    break
        probabilities.append(probability)

    return probabilities


def probability_of_at_least_one_streak(probabilities):
    prob_not_win_any = 1
    for prob in probabilities:
        prob_not_win_any *= (1 - prob)
    return 1 - prob_not_win_any


def probability_of_n(all_games, n, username):
    probabilities = calculate_streak(all_games, n, username)
    return probability_of_at_least_one_streak(probabilities)


def calc_probs(n, username):
    with open("gmhikaru_games_202210_202311.json", "r") as file:
        all_games = json.load(file)

    for i in range(n):
        print(f'Probability of a {i+1}-game streak: {probability_of_n(all_games, i + 1, username) * 100}%')


# months = {"months": []}	 # If you want to recreate the json file, embed the contents of game_definitions.txt here and uncomment the following code:

# def winning_chance(player_one_elo, player_two_elo):
#     return 1 / (1 + 10**((player_two_elo - player_one_elo) / 400))


# def get_player(player, chance):
#     return {'username': player['username'].lower(), 'rating': player['rating'], 'result': player['result'], 'winning_chance': chance}

		  
# def create_data_file():
#     all_games = []
#     for month in months['months']:
#         for game in month["games"]:
#             if game['rated']:
#                 elo_white = game['white']['rating']
#                 elo_black = game['black']['rating']
#                 summary = {
#                     'end_time': game['end_time'],
#                     'time_class': game['time_class'],
#                     'rules': game['rules'],
#                     'time_control': game['time_control'],
#                     'white': get_player(game['white'], winning_chance(elo_white, elo_black)),
#                     'black': get_player(game['black'], winning_chance(elo_black, elo_white))}
#                 all_games.append(summary)

#     print(f'{len(all_games)} games selected')
    
#     with open("gmhikaru_games_202210_202311.json", "w") as file:
#         json.dump(all_games, file, indent=4)

# create_data_file()

if __name__ == '__main__':
    calc_probs(100, 'hikaru')
    


