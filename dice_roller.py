import random
def main():
	dice_rolls = int(input("How many inputs"))
	dice_sum = 0
	dice_size = int(input("How many sides of dice"))
	for i in range(0,dice_rolls):
		roll = random.randint(1,6)
		dice_sum += roll
		if roll == 1:
			print('You rolled a critical fail')
		elif roll == dice_size:
			print('You rolled a critical success')
		else:
			print('You rolled a %d' % roll)
			print('Roll sum %d' % dice_sum)

if __name__== "__main__":
	main()
