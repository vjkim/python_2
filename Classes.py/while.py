import random


playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
	dmg = random.randrange(enemyatkl, enemyatkh)
	playerhp = playerhp - dmg

	if playerhp <= 30:
		playerhp = 30

	print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

	if playerhp == 30:
		print("YOu have low health. You've been teleported to the nearest inn.")
		break


	

	if playerhp == 0:
		print("You have died. You can not respawn, as you are dead.")