# Version 1.2:  bugfix involving failure to open file [2018 Dec 3]
# Version 1.1:  bugfix involving random seed [2018 Nov 27]

from generator import Generator
from string import ascii_uppercase
import random

src = None
while not src:
    filename = input("Input filename? ")
    try:
        fp = open(filename)
        src = fp.read()
        fp.close()
    except IOError:
        print("Unable to open file", filename)


n = 0
while not 0 < n <= len(src):
    try:
        n = int(input("What value of n? "))
        if n <= 0:
            print("Must choose positive n")
        if n > len(src):
            print("n cannot be longer than original text length")
    except ValueError:
        print("Invalid integer")

total = 0
while not 0 < total:
    try:
        total = int(input("How many characters of output are desired? "))
        if total <= 0:
            print("Must choose positive value")
    except ValueError:
        print("Invalid integer")


seed = None
print("""If you would like to fix the random number generator with a seed,
please enter a string to serve as your seed. Otherwise, just press return.""")
seed = input("Seed: ").strip()
if not seed:
    seed = ''.join(random.choice(ascii_uppercase) for _ in range(6))
    print('Using seed:', seed)
random.seed(seed)

model = Generator(src, n)

default = filename.split('/')[-1].split('.')[0] + '_' + str(n) + '.txt'

output = None
while not output:
    filename = input("Output filename? [default: %s] " % default)
    if not filename:
        filename = default
    try:
        output = open(filename,'w')
    except IOError:
        print("Unable to open file", filename)

for _ in range(total):
    next = model.nextChar()
    if next is '':
        break
    output.write(next)

output.close()
