import random


def main():
    print("Welcome to BLACKJACK GAME")
    print("Do you want to enter your own deck ? (1 for YES, 0 for NO)")

    user_deck = []
    default_deck = []

    choice = int(input("Enter your choice: "))
    choice_flag = False

    if choice == 1:
        choice_flag = True
        for i in range(0, 52):
            val = int(input("Enter %dth card for deck:" % (i + 1)))
            while val < 0 or val > 51:
                print("Please enter number between 0 and 52")
                val = int(input("Enter %dth card for deck:" % (i + 1)))
            user_deck.append(val)

    if choice_flag == 1:
        decision = []
        for each in range(1):
            print(user_deck)
            decision.append(BJ(user_deck, 0))
        decision.sort()

        print("Maximum earning: " + str(sum(decision)) + "$")

    elif choice == 0:

        print("Do you want to shuffle the deck ? (1 for YES, 0 for NO)")
        shuffleChoice = int(input("Enter your choice: "))

        while shuffleChoice < 0 or shuffleChoice > 1:
            print("Please enter valid value!!!")
            print("Do you want to shuffle the deck ? (1 for YES, 0 for NO)")
            shuffleChoice = int(input("Enter your choice: "))

        if shuffleChoice == 1:
            default_deck = shuffle()


        elif shuffleChoice == 0:
            default_deck = [27, 22, 29, 6, 24, 19, 21, 18, 51, 3, 40, 12, 5, 46, 14, 2, 34,
                            45, 16, 30, 23, 8, 42, 49, 7, 11, 25, 32, 26, 0, 4, 36, 10, 33, 35,
                            47, 9, 50, 15, 31, 37, 38, 17, 48, 28, 39, 13, 1, 20, 44, 43, 41]

    if choice_flag == 0:

        decision = []

        for each in range(1):
            print(default_deck)
            decision.append(BJ(default_deck, 0))

        decision.sort()

        print("Maximum earning: " + str(sum(decision)) + "$")


def BJ(deck, i):
    options = []

    if len(deck) - i < 4:
        return 0

    for p in range(2, len(deck) - i - 1):
        hand = deal(deck, i)
        dealer = deal(deck, i + 1)
        if len(deck[i + 4:i + p + 2]) > 0:
            hand += deck[i + 4:i + p + 2]

        if earning(hand) > 21:
            options.append(-1 + BJ(deck, i + p + 2))  # bust
            break
        d = 0
        for d in range(2, len(deck) - i - p):
            if len(deck[i + p + 2:i + p + d]) > 0:
                dealer += deck[i + p + 2:i + p + d]
            if earning(dealer) >= 17:
                break
        if earning(dealer) > 21:  # dealer bust
            dealer = []
        options.append((compare(earning(hand), earning(dealer)) + BJ(deck, i + p + d)))

    return max(options)


def compare(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


"I wrote shuffle () function in order to re-test program again. "


def shuffle():
    deck = [27, 22, 29, 6, 24, 19, 21, 18, 51, 3, 40, 12, 5, 46, 14, 2, 34,
            45, 16, 30, 23, 8, 42, 49, 7, 11, 25, 32, 26, 0, 4, 36, 10, 33, 35,
            47, 9, 50, 15, 31, 37, 38, 17, 48, 28, 39, 13, 1, 20, 44, 43, 41]
    random.shuffle(deck)
    return deck


def deal(deck, i):
    cards = [deck[i] % 13, deck[i + 1] % 13]
    return cards


def hit(deck, i):
    return deck[i]


""" How earning() function works?

    I take mod of each card because for my deck logic 0,13,26,39 are Ace. If card % 13 is equal to 1 then I understand
    this is Ace.
    
    Same think for J,Q,K. J=10,Q=11,K=12 all equal 10 points.
    
    For Ace, I calculate the total summation for both values(1,11) of ACE, if +11 is not cause of bust then I used 11,
    otherwise Ace are used as 1 point.
"""


def earning(hand):
    total = 0
    for each in hand:
        if each == 0:
            if total + 11 <= 21:
                total += 11
            else:
                total += 1

        elif each == 10:
            total += 10

        elif each == 11:
            total += 10

        elif each == 12:
            total += 10
        else:
            total += each

    return total


main()
