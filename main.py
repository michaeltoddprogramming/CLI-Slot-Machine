import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 5,
    "B": 4,
    "C": 2,
    "D": 0.5
}

def get_Slot_Machine_Spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 
    
    # EACH OF THESE NESTED LISTS WILL REPRESENT THE VALUES IN OUR COLUMNS
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_Machine(columns):
    # TRANSPOSING
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
            
        print()
                
    

def deposit():
    while True:
        amount = input("What would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0, Begin broke is not cool!")
        else:
            print("Please enter a number.")
            
    return amount

def get_Num_Of_Lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("Enter a Valid Number of lines! Between 1 and "+str(MAX_LINES)+"")
        else:
            print("Please enter a number.")
            
    return lines

def get_Bet():
    while True:
        amount = input("What would you like to Bet on each line? R")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between R{MIN_BET} - R{MAX_BET}")
        else:
            print("Please enter a number.")
            
    return amount
    
def check_Winnings(columns, lines, bet, values):
    winnings = 0
    winnning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnning_lines.append(line + 1)
        
    return winnings, winnning_lines
    
def gameLoopSpin(balance):
    lines = get_Num_Of_Lines()
    while True:
        bet = get_Bet()
        totalBet = bet * lines
        
        if totalBet > balance:
            print(f"Insufficient Funds! Your current balance is: R{balance}")
        else:
            break
            

    totalBet = bet * lines
    print(f"You are betting R{bet} on {lines} lines. Total bet is equal to: R{totalBet}")
    
    slots = get_Slot_Machine_Spin(ROWS, COLS, symbolCount)
    print_slot_Machine(slots)
    winnings, winnings_lines = check_Winnings(slots, lines, bet, symbolValue)
    print(f"You won R{winnings}")
    print(f"You won on lines:", *winnings_lines)
    return winnings - totalBet
    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is R{balance}")
        answer = input("Press Enter to play (q to quit)")
        if answer == "q":
            break
        balance += gameLoopSpin(balance)
    
    print(f"You left with R{balance}")

main()