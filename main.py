from random import shuffle, choice
import os
import time

suits = {'spade': '♠',
        'heart': '♥',
        'club': '♣',
        'diamond': '♦'}
numbers = ['A', '2', '3', '4', '5', '6', '7',
           '8', '9', '10', 'J', 'Q', 'K']
win_text="""
Yb  dP  dP"Yb  88   88     Yb        dP  88  88b 88
 YbdP  dP   Yb 88   88      Yb  db  dP   88  88Yb88
  8P   Yb   dP Y8   8P       YbdPYbdP    88  88 Y88
 dP     YbodP  `YbodP'        YP  YP     88  88  Y8
"""
lose_text = """
Yb  dP  dP"Yb  88   88     88      dP"Yb  .dP"Y8 888888
 YbdP  dP   Yb 88   88     88     dP   Yb `Ybo." 88__
  8P   Yb   dP Y8   8P     88  .o Yb   dP o.`Y8b 88""
 dP     YbodP  `YbodP'     88ood8  YbodP  8bodP' 888888
"""
game_over_text = '''
 dP""b8    db    8b    d8 888888      dP"Yb  Yb    dP 888888 88""Yb
dP   `"   dPYb   88b  d88 88__       dP   Yb  Yb  dP  88__   88__dP
Yb  "88  dP__Yb  88YbdP88 88""       Yb   dP   YbdP   88""   88"Yb
 YboodP dP""""Yb 88 YY 88 888888      YbodP     YP    888888 88  Yb
'''

def get_cards():
	cards = []
	for i in range(4):
		for number in numbers:
			for suit in suits.values():
				cards.append((number, suit))
	shuffle(cards)
	return cards

def get_card(cards):
	card = choice(cards)
	cards.remove(card)
	return card

def calculate(cards):
	sum = 0
	for card in cards:
		if card[0] in 'JQK':
			sum += 10
		elif card[0].isdigit():
			sum += int(card[0])
		else:
			if sum + 11 > 21:
				sum += 1
			else:
				sum += 11
	return sum

def output(cards, is_player=True):
	sum = calculate(cards)
	if is_player:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"Your sum is {sum} and hand is:")
	else:
		print(f"\nDealer's sum is {sum} and hand is:")
	hand = ['', '', '', '', '']
	for card in cards:
		hand[0] = hand[0] + "┌─────┐  "
		if card[0] == '10':
			hand[1] = hand[1] + f"|{card[0]}   |  "
			hand[2] = hand[2] + f"|  {card[1]}  |  "
			hand[3] = hand[3] + f"|   {card[0]}|  "
		else:
			hand[1] = hand[1] + f"|{card[0]}    |  "
			hand[2] = hand[2] + f"|  {card[1]}  |  "
			hand[3] = hand[3] + f"|    {card[0]}|  "
		hand[4] = hand[4] + "└─────┘  "
	for _ in hand:
		print(_)

def result(player, dealer):
	output(player)
	output(dealer, is_player=False)

	if calculate(player) > 21 or calculate(dealer) >= calculate(player) and calculate(dealer) <= 21:
	    print(lose_text)
	else:
	    print(win_text)

def play(cards):
	player = []
	dealer = []

	player.append(get_card(cards))
	dealer.append(get_card(cards))
	player.append(get_card(cards))
	dealer.append(get_card(cards))

	while True:
		output(player)
		sum = calculate(player)

		if sum > 21:
			break

		move = input("Choose a move: \n 1) Hit \n 2) Stand \n")
		if move == '1':
			player.append(get_card(cards))
		elif move == '2':
			break

	if calculate(player) > 21:
		print(lose_text)
		return

	while True:
		if calculate(dealer) < calculate(player):
			output(player)
			output(dealer, is_player=False)
			dealer.append(get_card(cards))
			time.sleep(0.85)
		else:
			break

	result(player, dealer)

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	cards = get_cards()
	while True:
		play(cards)
		if len(cards) < 10:
			os.system('cls' if os.name == 'nt' else 'clear')
			print(game_over_text)
			break
		inp = input("Play again? Yes or No (Leave it to continue): ")
		if inp.lower() == 'no':
			break


