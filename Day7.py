import sys
import HelperFunctions

day_number = 7

CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class Hand():
    def __init__(self, data):
        d = data.split(' ')
        self.hand = d[0]
        self.bid = int(d[1])
        self.score = self.GetScore()

    def GetScore(self):
        counts = {e:self.hand.count(e) for e in set(self.hand)}
        counts2 = list(counts.values())
        counts2.sort(reverse=True)

        c = counts2[0]
        if c == 5:
            return 7 #5 of kind
        if c == 4:
            return 6 #4 of kind
        if c == 3:
            if counts2[1] == 2:
                return 5 #full house
            else:
                return 4 #3 of a kind
        if c == 2:
            if counts2[1] == 2:
                return 3 #2 pair
            else:
                return 2 #1 pair
        if c == 1:
            return 1 #High card
        
    def GetBid(self):
        return self.bid
    
    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        else:
            for i in range(5):
                if self.hand[i] != other.hand[i]:
                    return CARD_ORDER.index(self.hand[i]) > CARD_ORDER.index(other.hand[i])
        return False


def Part1(input):
    result = 0

    hands = []

    for line in input.splitlines():
        hands.append(Hand(line))
    
    hands.sort()

    for i in range(len(hands)):
        result += (i+1) * hands[i].GetBid()        

    return result

CARD_ORDER_P2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
CARD_REPLACE = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class Hand2():
    def __init__(self, data):
        d = data.split(' ')
        self.hand = d[0]
        self.bid = int(d[1])
        self.score = self.GetScore(self.hand)

    def GetScore(self, hand):
        index = hand.find('J')
        if index >= 0:
            tempScore = 0
            for c in CARD_REPLACE:
                tempHand = hand
                tempHand = tempHand.replace('J',c,1)
                tempScore = max(self.GetScore(tempHand),tempScore)
            return tempScore
        else:
            counts = {e:hand.count(e) for e in set(hand)}
            counts2 = list(counts.values())
            counts2.sort(reverse=True)

            c = counts2[0]
            if c == 5:
                return 7 #5 of kind
            if c == 4:
                return 6 #4 of kind
            if c == 3:
                if counts2[1] == 2:
                    return 5 #full house
                else:
                    return 4 #3 of a kind
            if c == 2:
                if counts2[1] == 2:
                    return 3 #2 pair
                else:
                    return 2 #1 pair
            if c == 1:
                return 1 #High card
        
    def GetBid(self):
        return self.bid
    
    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        else:
            for i in range(5):
                if self.hand[i] != other.hand[i]:
                    return CARD_ORDER_P2.index(self.hand[i]) > CARD_ORDER_P2.index(other.hand[i])
        return False

def Part2(input):
    result = 0

    hands = []

    for line in input.splitlines():
        hands.append(Hand2(line))
    
    hands.sort()

    for i in range(len(hands)):
        result += (i+1) * hands[i].GetBid()        

    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')