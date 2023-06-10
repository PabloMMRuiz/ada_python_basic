import random
import os
import time
class Card:
    def __init__(self, suit, value) -> None:
        if(type(value)!=int):
            raise TypeError("Unknown card value")
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        val = "" #NOTE: actualizar python al 3.10
        if(self.value ==12): #Spanish language
            val ="Rey"
        elif(self.value==11):
            val ="Caballo"
        elif(self.value==10):
            val="Sota"
        elif(self.value==1):
            val="As"
        else:
            val = str(self.value)
        return(f"{val} de {self.suit}")
    
class Deck:
    def __init__(self, suits: list, intervals:list) -> None:
        cards = []
        for s in suits:
            for interval in intervals:
                for n in range(interval[0], interval[1]+1):
                    cards.append(Card(s, n))
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self) -> str:
        return str([str(c) for c in self.cards])
    
    def __len__(self)->int:
        return len(self.cards)
    
    def get_card(self) ->Card:
        return self.cards.pop(-1)
    
    def get_cards(self, n)->list:
        return self.cards[-n:]

    def add_card(self, c):
        self.cards.append(c)

    def add_cards(self, c_list):
        self.cards += c_list

    

def classic_spanish_solitaire():
    #Initialization
    deck = Deck(["oros", "copas", "espadas", "bastos"], [(1,7), (10,12)])
    deck.shuffle()
    table = {"1":[], "2":[], "3":[], "4":[]}
    for t in range(1, len(table)+1):
                    table[str(t)] = table[str(t)] + [deck.get_card()]
    print(f"Instructions: Type Kill to eliminate a card\nType Move to move a card to an empty column\nType End to finish a turn")
    time.sleep(5)
    turns = 9
    while turns>0:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(max(table.values(), key=lambda a:len(a)))):
            print(f"{str(table['1'][i] if i<len(table['1']) else '  ').ljust(15)} | {str(table['2'][i] if i<len(table['2']) else '  ').ljust(15)} | {str(table['3'][i] if i<len(table['3']) else '  ').ljust(15)} | {str(table['4'][i] if i<len(table['4']) else '  ').ljust(15)}")
        print("\n")
        command = input("Waiting for action: Move, Kill, End, Instructions:    ")
        if("Instructions" in command):
            print(f"\nInstructions: Type Kill 'column x', 'column y' to eliminate a card in column y using one from column x \nType Move 'column x', column y' to move a card from column x to column y \nType End to finish a turn")
            time.sleep(4)
        elif("Kill" in command):
            print("Killing...")
            from_col = input("Column to kill with (1,2,3,4)... ")
            to_col = input("Column to kill(1,2,3,4)... ")
            if(from_col not in table or to_col not in table):
                print("Unknown play")
            elif(from_col == to_col):
                print("Can't kill cards on the same column")
            elif(len(table[from_col]) <= 0 or len(table[to_col])<=0):
                print("Empty columns: use Move")
            elif(table[from_col][-1].suit != table[to_col][-1].suit):
                print("Not the same suit!")
            elif(table[from_col][-1].value !=1 and table[to_col][-1].value > table[from_col][-1].value):
                print("Can't kill cards with higher value")
            else:
                 table[to_col] = table[to_col][:-1]
            time.sleep(.5)
        elif("Move" in command):
            print("Moving...")
            from_col = input("Column to move from (1,2,3,4)... ")
            to_col = input("Column to move to (1,2,3,4)... ")
            if(from_col not in table or to_col not in table):
                print("Unknown play")
            elif(from_col == to_col):
                print("Can't kill cards on the same column")
            elif(len(table[to_col]) !=0):
                print("Destination column not empty")
            else:
                table[to_col].append(table[from_col].pop(-1))
            time.sleep(.5)
        elif("End" in command):
            for t in range(1, len(table)+1):
                table[str(t)] = table[str(t)] + [deck.get_card()]
            turns -=1
            time.sleep(.5)
    if(table["1"][0].value == 1 and table["2"][0].value == 1 and table["3"][0].value == 1 and table["4"][0].value == 1 ):
        print(f"You won")
    else:
        print("You lost")
    command = input("Play again? (y/n) ")
    if(command == "y"):
        classic_spanish_solitaire()
    else: return

if __name__ == "__main__":

    print(f"\n\n#####Iniciando juego#####\n\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    classic_spanish_solitaire()
    """c1 = Card("oros", 3)
    c2 = Card("bastos", 12)
    c3 = Card("bastos", 11)
    c4 = Card("bastos", 10)
    c5 = Card("copas", 6)
    c6 = Card("espadas", 1)
    cards = [c1, c2, c3, c4, c5, c6]
    for c in cards:
        print(c)

    d1 = Deck(["oros", "copas", "espadas", "bastos"], [(1,7), (10,12)])
    print(d1)
    print(len(str(d1).split(","))) #Number of cards
    d1.shuffle()
    print(d1)
    print(d1.get_card())
    print(len(str(d1).split(","))) #Number of cards. Should be one less
    print(d1)
    d1.add_card(Card("Perros", 26))
    print(d1)
    d1.add_cards(cards)
    print(len(str(d1).split(",")))"""

    


        