# Blackjack
- A terminal-based Blackjack game built in Python.
- Play against a computer dealer with a betting system, card score logic, and simple visuals.
- Includes basic card drawing with suits and handles Blackjack rules such as ace adjustments and dealer hitting below 17.

## Features
- Visual ASCII logo
- Simulated card drawing with suits
- Full Blackjack rules including ace value adjustment
- Dealer logic that hits until reaching 17 or more
- Betting system with persistent balance
- Game ends when balance reaches zero or user quits

## Tech Stack
- Python 3.X
- Standard libraries: `random`

## How to Play
1. Start with $1000.
2. Place a bet before each round.
3. Draw cards and decide whether to hit or stand.
4. Try to beat the dealer without going over 21.
5. Game continues until you choose to quit or run out of money.

## Setup and Installation
### 1. Clone the repository:
```bash
git clone https://github.com/rampalliprakhar/Blackjack.git
cd blackjack
```

### 2. Run the program:
```bash
python main.py
```

### 3. Sample Gameplay
```bash
Welcome to Blackjack!

You have $1000. How much would you like to bet? 200

Your bet: $200
Your hand: 9♠, 7♦
Computer's hand: Q♣ and a hidden card
Your current score: 16

Type 'y' to get another card, type 'n' to pass: y
Your hand: 9♠, 7♦, 5♥
Your current score: 21

Computer's hand: Q♣, 6♦, 7♠
Opponent went over. You win!
Your new balance is $1200
```

### 4. Project Structure
```bash
blackjack/
├── art.py         # Contains ASCII art logo
└── main.py        # Main game logic
```
