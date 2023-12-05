from random import randint, choice
import string
from itertools import permutations


def mutationA(seed: str)->str:
    """Remove a random byte"""
    l = len(seed)
    r = randint(0, l - 1)
    return seed[:r] + seed[r+1:]

def mutationB(seed: str)->str:
    """Swap adjacent bytes"""
    l = len(seed)
    r = randint(0, l - 2)
    return seed[:r] + seed[r + 1] + seed[r] + seed[r+2:]

def mutationC(seed: str)->str:
    """Insert a random byte"""
    l = len(seed)
    r = randint(0, l - 1)
    return seed[:r] + choice(string.ascii_letters) + seed[r:]

def mutationD(seed: str)->str:
    """Replace bytes with random values"""
    for i in range(randint(0, len(seed))):
        seed = mutationC(mutationA(seed))
    return seed

def mutationE(seed: str)->str:
    """Return a random permutation of the string. An expensive for longer seeds"""
    p = list(permutations(seed))
    r = randint(0, len(p) - 1)
    return "".join(p[r])

MUTATIONS_LIST = [mutationA,
             mutationB,
             mutationC,
             mutationD,
             ]

def select_mutation_function():
    return choice(MUTATIONS_LIST)