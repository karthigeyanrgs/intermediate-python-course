import random
def main():
	dice_rolls = 2
	dice_sum = 0
	for i in range(0,dice_rolls):
		roll = random.randint(1,6)
		dice_sum += roll
		print('You rolled a %d' % roll)
		print('Roll sum %d' % dice_sum)

if __name__== "__main__":
	main()
