import random
import art

print(art.logo)
acc = 1000


def player_sum():
    playersum = 0
    for i in player_card:
        playersum += cards[i]
    return playersum


def computer_sum():
    computersum = 0
    for i in computer_card:
        computersum += cards[i]
    return computersum


def comphit():
    computer_card.append(random.choice(list(cards)))
    computersum = computer_sum()
    if computer_card[-1] == 'A' and computersum > 21:
        computer_card[-1] = '1'
    computer()


def compshow():
    print("COMPUTER : ", end='')
    computersum = 0
    for i in computer_card:
        print(f"{i}, ", end='')
        computersum += cards[i]

    print(f"Total points = {computersum}")


def computer():
    while True:
        computersum = 0
        for i in computer_card:
            computersum += cards[i]
        if computersum < 18:
            comphit()
        else:
            break


def playerhit():
    player_card.append(random.choice(list(cards)))
    playersum = player_sum()
    if player_card[-1] == 'A' and playersum > 21:
        player_card[-1] = '1'
    print("PLAYER :", end='')
    for i in player_card:
        print(f"{i}, ", end='')
    print(f"Total points = {playersum}")
    return player()


def playershow():
    for i in player_card:
        playersum = 0
        for i in player_card:
            playersum += cards[i]


def comparethis():
    global acc
    playersum = player_sum()
    computersum = computer_sum()
    if computersum > 21 and playersum < 22:
        print("Computer bust. Player Wins!")
        acc = acc + (bet * 2)
        return True
    if computersum > 21 and playersum > 21:
        print("Both bust. Its a Draw!")
        return True


def compare():
    global acc
    playersum = player_sum()
    computersum = computer_sum()
    if playersum > computersum:
        print("player wins")
        acc = acc + (bet * 2)
    elif computersum > playersum:
        print("computer wins")
        acc = acc - (bet * 2)
    else:
        print("draw")


def player():
    global acc
    playersum = player_sum()
    if playersum > 21:
        print("You have bust. Computer WINS!")
        acc = acc - (bet * 2)
        return True
    else:
        hit = input("Do you want to 'hit' or 'show'?")
        if hit == 'hit':
            return playerhit()
        else:
            playershow()


while True:
    if acc <= 0:
        print("No money to bet")
        break
    print()
    play = input(
        f"Do you want to experience the world of Black Jack? y or n?                    Bank Balance : ${acc}\n"
    )
    if play == 'n':
        break
    while True:
        bet = int(input("What is your bet?"))
        if bet <= acc:
            break
        else:
            print("NOT POSSIBLE, BET A REASONABLE PRICE")
    computer_card = []
    player_card = []
    # cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = {
        'A': 11,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    computer_card.append(random.choice(list(cards.keys())))
    computer_card.append(random.choice(list(cards.keys())))
    player_card.append(random.choice(list(cards.keys())))
    player_card.append(random.choice(list(cards.keys())))

    print(
        f"COMPUTER : (?,{computer_card[1]}) total points = {cards[computer_card[1]]}"
    )
    print(
        f"PLAYER : ({player_card[0]},{player_card[1]})  total points = {cards[player_card[0]] + cards[player_card[1]]}"
    )

    computer()
    pl = player()
    compshow()
    if pl:
        continue
    ct = comparethis()
    if ct:
        continue
    compare()
