import random

card_type = ['梅花', '红桃', '黑桃', '方片']
card_number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = [j + i for i in card_number for j in card_type]

random.shuffle(cards)
print(cards)
