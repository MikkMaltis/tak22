import random

def choose_card():
    next_suit = random.choice(suits)
    next_rank = random.choice(ranks)

    used_ranks.append(next_suit + next_rank)

    while (next_rank + next_suit) in used_cards:
        next_suit = random.choice(suits)
        next_rank = random.choice(ranks)

used_cards.append(next_suit + next_rank)

return [next_suit, next_rank]

print(next_suit, next_rank)

print(used_cards)

suits = ['ärtu', 'poti', 'risti', 'ruutu']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'poiss', 'emand', 'kuningas', 'äss' ]
used_cards = []