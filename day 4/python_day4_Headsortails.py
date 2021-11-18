import random
##random.random() creates float
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")