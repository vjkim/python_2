import random


class Enemy:
	hp = 200


	def __init__(self, atkl, atkh):
		self.atkl = atkl
		self.atkh = atkh


	# Blueprint for objects

	def getAtk(self):
		print("Atk is", self.atkl)

	def getHp(self):
		print("HP is", self.hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()


'''


playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
	dmg = random.randrange(enemyatkl, enemyatkh)
	playerhp = playerhp - dmg

	if playerhp <= 30:
		playerhp = 30

	print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

	if playerhp > 30:
		continue

	print("YOu have low health. You've been teleported to the nearest inn.")
	break
	

	if playerhp == 0:
		print("You have died. You can not respawn, as you are dead.")
		'''