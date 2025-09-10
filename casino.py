import time
import random

cash = int(1000)
over_l = True

list_game = ["crash", "sapper"]  
def save_cash(amount):
    with open('casino_money.txt', 'w') as file:
        file.write(str(amount))
def load_cash():
    try:
        with open('casino_money.txt', 'r') as file:
            return float(file.read().strip())
    except (FileNotFoundError, ValueError):
        # Если файла нет или он поврежден, вернем стартовую сумму
        return 1000.0  # Стартовая сумма
def clear_l():
	print("""
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	""")
def menu():
  print("Casino 1.0")
  print("Enter game casino")
  print("Enter 'help' for list game")
    
def sapper():
	i = 0
	list_cells = [0] * 6
	game_win = ["GREAT!","EASY WIN!","GOOD!","COOL!","CRAZY!"]
	print("game SAPPER started")
	global cash
	while True:
		try:
			global over_l
			if over_l == False:
				clear_l()
				menu()
				return
			print(f"you cash - ${cash}")
			bet = int(input("Your bet - $")) 
			if bet < 10:
				print("you can't bet less than 10!")
				continue
			elif bet > cash:
				print("insufficient funds!")
				continue
			
				
		except ValueError:
			print("Invalid input!")
			continue
		passw = str(input(f"your bet ${bet} ? Y/n \n")).strip()
		if passw in ['Y', 'y', 'Yes', 'yes']:
			print("Starting...")
			time.sleep(0.5)
		else:
			continue
		try:
			field = int(input("enter size field sapper: 3x3-(0),3x4-(1),4x4-(2)\n"))
			if field in [0,1,2]:
				print("ok")
			else:
				print("not found...")
				continue
				
		except ValueError:
			print("invalid input")
			continue
		print("the standard number of mines is set (6)")
		time.sleep(0.5)
		if field == 0:
			field_game = 3 * 3
			x = 2.75
		elif field == 1:
			field_game = 3 * 4
			x = 1.65
		elif field == 2:
			field_game = 4 * 4
			x = 1.25
		list_true = [0] * field_game
		list_cells = random.sample(range(1, field_game + 1), 6)
		i = 0
		while True:
			if i in list_cells:
				list_true[i] = False
			else:
				list_true[i] = True
			
			
			i = i + 1
			if i > field_game - 1:
				break
		list_false = ["NULL"] * field_game
		print("game started!")
		i = 0
		main_x = 0
		wins = 0
		while True:
			try:
				selected_numbers = [val for val in list_false if val != 'NULL']
				print(f"your winnings are ${bet * main_x} and x{main_x}")
				print("enter number cell for select,selected cells - " , selected_numbers)
				print("Enter 'exit' or Ctrl+C to claim your prize")
				cell = input(">")
				if cell == "exit":
					cash = bet * main_x
					save_cash(cash)
					sapper()
				cell = int(cell)
				if cell in list_false:
					print("you have already selected this cell!")
				elif list_true[cell] == True:
					list_false[i] = cell
					if main_x == 0:
						main_x = x
					else:
						main_x = main_x + x - 1
					print(random.choice(game_win))
					i = i + 1
				elif list_true[cell] == False:
					cash = cash - bet
					print("GAME OVER!")
					save_cash(cash)
					pp = input("play again?\n >")
					if pp == "yes":
						sapper()
					else:
						over_l = False
						break
			except ValueError:
				print("invalid input!")
			except IndexError:
				print(f"not more {field_game - 1}!") 
			except KeyboardInterrupt:
				cash = bet * main_x
				save_cash(cash)
				sapper()	
def crash():
	pass
    
def enter_l():
  game = input("> ").lower().strip()  
    
  if game == "help":
    print("Available games:", list_game)
    return False 
  elif game in list_game:
    print(f"Starting {game}...")
    time.sleep(0.1)
    return game 
  else:
    print("Game not found!")
    return False
cash = load_cash()
menu()
def main():
	while True:
		ps = enter_l()
		if ps == False:
		  continue
		elif ps in list_game:
			if ps == list_game[0]:
				crash()
				continue
			elif ps == list_game[1]:
				sapper()
				continue
main()
		
