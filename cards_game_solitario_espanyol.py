import random
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


if __name__ == "__main__":
    c1 = Card("oros", 3)
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
    d1.shuffle()
    print(d1)


        