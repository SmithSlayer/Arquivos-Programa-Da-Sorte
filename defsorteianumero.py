import random

def sorteianumero(x):
  if x == 1:
    numsorteado = random.randint(1, 50)
    return numsorteado
  elif x == 2:
    numsorteado = random.randint(1, 100)
    return numsorteado
  elif x == 3:
    numsorteado = random.randint(1, 1000)
    return numsorteado
  elif x >= 4:
    return False