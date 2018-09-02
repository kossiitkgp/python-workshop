import random
import string
import time

def random_string_gen(len):
    return ''.join(random.choice(string.ascii_letters+string.punctuation+" ") for i in range(len))

orig = "KOSS Python Programming classes"

remain = list(range(len(orig)))

updated = [' ' for _ in range(len(orig))]

counter = 0

def check(orig,remain):
    rand = random_string_gen(len(orig))
    for i in remain:
        if orig[i] == rand[i]:
            updated[i] = rand[i]
            remain.remove(i)
        print(''.join(updated),end='\r')
        # time.sleep(0.005)

while True:
    if orig == ''.join(updated):
        print(end="\n")
        print('This took',counter,'iterations!')
        break
    check(orig,remain)
    counter = counter + 1