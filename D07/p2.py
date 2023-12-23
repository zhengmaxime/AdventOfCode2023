from collections import Counter

INPUT_FILE = 'input'

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

card_values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = int(bid)
        self.type = get_hand_type(cards)

    def __lt__(self, other):
        if self.type == other.type:
            l1 = [ card_values.index(elt) for elt in self.cards ]
            l2 = [ card_values.index(elt) for elt in other.cards ]
            return l1 < l2
        return self.type < other.type

    def __str__(self):
        return f'{self.cards} {self.bid}'

    def __repr__(self):
        return str(self)


def get_hand_type(cards: str) -> int:
    letters = Counter(cards)
    if 'J' in letters.keys() and len(letters) > 1:
        most_common_letter = letters.most_common(1)[0][0]
        if 'J' == most_common_letter: # two most common objects [1]
            most_common_letter = letters.most_common(2)[1][0]
        letters[most_common_letter] += letters['J']
        letters.pop('J')
    if len(letters) == 1:
        return FIVE_OF_A_KIND
    if len(letters) == 5:
        return HIGH_CARD
    if len(letters) == 4:
        return ONE_PAIR
    val = letters.most_common(1)[0][1]
    if len(letters) == 2:
        if val == 4:
            return FOUR_OF_A_KIND
        if val == 3:
            return FULL_HOUSE
    if len(letters) == 3:
        if val == 3:
            return THREE_OF_A_KIND
        if val == 2:
            return TWO_PAIR
    return 0

assert get_hand_type('AAAAA') == FIVE_OF_A_KIND
assert get_hand_type('23456') == HIGH_CARD
assert get_hand_type('A23A4') == ONE_PAIR
assert get_hand_type('AA8AA') == FOUR_OF_A_KIND
assert get_hand_type('23332') == FULL_HOUSE
assert get_hand_type('TTT98') == THREE_OF_A_KIND
assert get_hand_type('23432') == TWO_PAIR

# Part 2: J cards can pretend to be whatever card is best for the purpose of determining hand type

assert get_hand_type('TJJJ5') == FOUR_OF_A_KIND
assert get_hand_type('JJJJJ') == FIVE_OF_A_KIND
assert get_hand_type('AAAJJ') == FIVE_OF_A_KIND
assert get_hand_type('QJJQ2') == FOUR_OF_A_KIND
assert get_hand_type('QQQJA') == FOUR_OF_A_KIND

# %%
hands = []
for line in open(INPUT_FILE):
    hand, bid = line.split()
    hands.append(Hand(hand, bid))
#print(sorted(hands))
print(sum([ x.bid * (i + 1) for i, x in enumerate(sorted(hands))]))
