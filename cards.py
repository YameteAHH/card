# Angelica Kristianne G. Pre
# Maria Christina C. Salvador
# BSCS-2
# February 23, 2024

#Programming Language Activity

lists_of_cards = [ 'King of Clubs (Black)', 'King of Hearts (Red)',
                   'King of Spades (Black)', 'King of Diamonds (Red)',
                   'Queen of Clubs (Black)', 'Queen of Hearts (Red)',
                   'Queen of Spades (Black)', 'Queen of Diamonds (Red)' ]

left = []
right = []

def shuffle_cards(cards, higher_deck, lower_deck):
    for index in range(1, len(cards) + 1):
        if index % 2 == 0:
            higher_deck.append(cards[index - 1])
        else:
            lower_deck.append(cards[index - 1])


print("Hi there, let's play a game.\nThink of any cards and I will guess it.")

# First Shuffling of Cards
shuffle_cards(lists_of_cards, right, left)
print('\nIs your card in here?')
for card in right:
    print(card)

while True:
    user_input = input('= ')
    if user_input.lower() == 'yes':
        lists_of_cards = right + left
    elif user_input.lower() == 'no':
        lists_of_cards = left + right
    else:
        print('Yes\' or \'No\' answers only')
        continue
    break

left = []
right = []

# Second Shuffling of Cards
shuffle_cards(lists_of_cards, right, left)
print('\nIs your card in here?')
for card in right:
    print(card)

while True:
    user_input = input('= ')
    if user_input.lower() == 'yes':
        lists_of_cards = left + right
    elif user_input.lower() == 'no':
        lists_of_cards = right + left
    else:
        print('Yes\' or \'No\' answers only')
        continue
    break

left = []
right = []

# Third Shuffling of Cards
shuffle_cards(lists_of_cards, right, left)
print('\nIs your card in here?')
for card in right:
    print(card)

while True:
    user_input = input('= ')
    if user_input.lower() == 'yes':
        lists_of_cards = right + left
    elif user_input.lower() == 'no':
        lists_of_cards = left + right
    else:
        print('Yes\' or \'No\' answers only')
        continue
    break

left = []
right = []

# Final Guess
shuffle_cards(lists_of_cards, right, left)
king_or_queen_determinant = right[0]

new_left = []
new_right = []

left.reverse()

shuffle_cards(left, new_right, new_left)
color_determinant = new_right[0]
suit_determinant = new_left[0]
the_card = new_left[1]

print(f'\nYou are thinking of {the_card}')