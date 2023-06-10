class Card:
    def __init__(self, suit, value) -> None:
        if(type(value)!=int or (7<value<=0 and 12<value<10)):
            raise ValueError("Unknown card value")
        if(type(suit)!=str or suit not in {"copas", "espadas", "bastos", "oros"}):
            raise ValueError("Unknown card suit")
        
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        val = "" #NOTE: actualizar python al 3.10
        if(self.value ==12):
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

        