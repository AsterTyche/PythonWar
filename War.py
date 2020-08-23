from random import shuffle


class Deck:
    def __init__(self):
        self.cards = list(range(1, 14))*4

deck = Deck()
shuffle(deck.cards)

plone = deck.cards[:26]
pltwo = deck.cards[26:]

moves = 0

def War():
    global plone
    global pltwo
    global moves
    
    while len(plone) != 52 or len(plone) != 0:
        try:
            cardone = plone[0]
            cardtwo = pltwo[0]
        except:
            break
        plone.pop(0)
        pltwo.pop(0)
        if cardone > cardtwo:
            plone.append(cardone)
            plone.append(cardtwo)
        elif cardtwo > cardone:
            pltwo.append(cardone)
            pltwo.append(cardtwo)
        else:
            if len(plone)<4:
                pltwo = deck.cards
                moves += 1
                break
            if len(pltwo)<4:
                plone = deck.cards
                moves += 1
                break
            tie(cardone, cardtwo, [])
        moves += 1
    if len(plone)>len(pltwo):
        print("Player one won with %s moves!" % (str(moves)))
    else:
        print("Player two won with %s moves!" % (str(moves)))
        
def tie(cardone, cardtwo, remaining):
    global plone
    global pltwo
    global moves
    moves += 1
    if len(plone)<4:
        wartwo = deck.cards
        return
    if len(pltwo)<4:
        warone = deck.cards
        return
    warone = plone[:4]
    wartwo = pltwo[:4]
    b = 0
    for x in range(4):
        try:
            plone.pop(x)
            pltwo.pop(x)
        except:
            return
        if warone[x] > wartwo[x]:
            b += 1
        elif warone[x] < wartwo[x]:
            b -= 1
    if b > 0:
        for x in warone:
            plone.append(x)
        for y in wartwo:
            plone.append(y)
        for x in remaining:
            plone.append(x)
        plone.append(cardone)
        plone.append(cardtwo)
    elif b < 0:
        for x in warone:
            pltwo.append(x)
        for y in wartwo:
            pltwo.append(y)
        for x in remaining:
            pltwo.append(x)
        pltwo.append(cardone)
        pltwo.append(cardtwo)
    else:
        for x in wartwo:
            warone.append(x)
        tie(cardone, cardtwo, warone)

War()
