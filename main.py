import random
from time import perf_counter

def isPrime(testPrime):
  i = 2
  x = 0
  while True:
    if testPrime/2 <= i:
      return True
    else:
      pass
    #Percentage Meter
    if x == int((i/(testPrime/2))*100):
      pass
    else:
      x = int((i/(testPrime/2))*100)
      print(str(x) + '% done!')
      pass
    if testPrime % i == 0:
      return False
    #Step Optimization
    if i == 2:
      i = i + 1
    elif i > 2:
      i = i + 2

def findPrimes(minNumber):
  for i in range(minNumber, (minNumber*2)):
    if isPrime(i):
      print(str(i) + ' is a prime!')
      break
    else:
      pass

def random_number_generator():
  return random.randrange(10000000, 100000000)

if __name__ == "__main__":
  x = perf_counter()
  findPrimes(random_number_generator())
  print(str(perf_counter() - x) + ' seconds elapsed')