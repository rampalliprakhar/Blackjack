from art import logo
import random

def arrange_card():
    """Returns a random card from the deck (with rank and suit)"""
    suits = ['♠', '♣', '♦', '♥']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card = random.choice(ranks)
    suit = random.choice(suits)
    return f"{card}{suit}"

def calculate_score(cards):
    """Returns the sum of all the cards in the list as the score"""
    score = 0
    ace_count = 0
    for card in cards:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(rank)

    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    return score

def display_cards(player, player_cards, is_computer=False):
    """Display the player's cards nicely."""
    if is_computer:
        print(f"{player}'s hand: {', '.join(player_cards[:-1])} and a hidden card")
    else:
        print(f"{player}'s hand: {', '.join(player_cards)}")

def compare(u_score, c_score, bet, balance):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw!!", balance
    elif c_score == 0:
        balance -= bet
        return f"Lose, opponent has Blackjack!!!", balance
    elif u_score == 0:
        balance += bet
        return f"Win with a Blackjack!", balance
    elif u_score > 21:
        balance -= bet
        return f"You went over. You lose !!!", balance
    elif c_score > 21:
        balance += bet
        return f"Opponent went over. You win!", balance
    elif u_score > c_score:
        balance += bet
        return f"You win!", balance
    else:
        balance -= bet
        return f"You lose!!!", balance

def place_bet(balance):
    """Allow the user to place a bet."""
    while True:
        bet = input(f"You have ${balance}. How much would you like to bet? ")
        if bet.isdigit() and int(bet) <= balance:
            return int(bet)
        else:
            print("Invalid bet amount. Please enter a valid bet.")

def blackjack():
    """Main blackjack game loop with betting system."""
    balance = 1000
    print(logo)
    print("Welcome to Blackjack!")

    while balance > 0:
        bet = place_bet(balance)
        user_cards = [arrange_card(), arrange_card()]
        computer_cards = [arrange_card(), arrange_card()]
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        is_game_over = False

        print(f"\nYour bet: ${bet}")
        
        while not is_game_over:
            display_cards("Your", user_cards)
            display_cards("Computer", computer_cards, is_computer=True)
            
            print(f"Your current score: {user_score}")
            if user_score == 21:
                print("Blackjack!")
                is_game_over = True

            if user_score > 21:
                print("You busted!")
                is_game_over = True
            elif computer_score == 21:
                print("Computer got Blackjack!")
                is_game_over = True
            else:
                user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_choice == "y":
                    user_cards.append(arrange_card())
                    user_score = calculate_score(user_cards)
                else:
                    is_game_over = True

        while computer_score < 17:
            computer_cards.append(arrange_card())
            computer_score = calculate_score(computer_cards)

        display_cards("Your", user_cards)
        display_cards("Computer", computer_cards)

        result, balance = compare(user_score, computer_score, bet, balance)

        print(result)
        print(f"Your new balance is ${balance}.")

        if balance <= 0:
            print("You're out of money! Game over.")
            break

        play_again = input("Do you want to play again? Type 'y' for Yes or 'n' for No: ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        
blackjack()