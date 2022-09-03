import random

question = ['Сколько вам лет?', 'Где вы работаете?', 'Ваше любимое блюдо?']
random.shuffle(question)
players = []
dare = ['Попрыгай', 'Присядь', 'Пробегись']
random.shuffle(dare)


def add_players(players):
    while True:
        name = input('Enter a player name: ')
        players.append(name)
        if len(players) >= 2:
            next_player = input(
                f'Need more player? '
                f'(write "yes" to add a player, or ENTER to start the game): '
            )
            if str.lower(next_player) == str.lower('y') or str.lower(next_player) == str.lower('yes'):
                continue
            else:
                break

    return players


def game(question, dare, *players):
    while True:
        game = input('Are we playing? (+/y или -/n): ')

        if game == '+' or game == 'y':
            for player in players:
                print(f'Your turn, {random.choice(player)}')
                player_choise = input('Truth or dare?, (t\d): ')
                if player_choise == str.lower('t') or player_choise == str.lower('Truth'):
                    question_ind = random.randint(0, len(question) - 1)
                    print(question[question_ind])
                    question.pop(question_ind)
                elif player_choise == str.lower('d') or player_choise == str.lower('Dare'):
                    question_ind = random.randint(0, len(question) - 1)
                    print(dare[question_ind])
                    question.pop(question_ind)
                else:
                    question_ind = random.randint(0, len(question) - 1)
                    print(question[question_ind])
                    question.pop(question_ind)
                    dare_ind = random.randint(0, len(dare) - 1)
                    print(dare[dare_ind])
                    question.pop(dare_ind)
        else:
            print(f'Thanks for playing!')
            break


add_players(players)
game(question, dare, players)
