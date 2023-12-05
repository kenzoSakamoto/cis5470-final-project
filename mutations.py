from random import randint, choice
import string
from itertools import permutations

def mutationA(seed: str)->str:
    """Remove a random byte"""
    l = len(seed)
    if (l <= 0):
        return choice(string.ascii_letters)
    r = randint(0, l - 1)
    return seed[:r] + seed[r+1:]

def mutationB(seed: str)->str:
    """Swap adjacent bytes"""
    l = len(seed)
    if (l <= 0):
        return choice(string.ascii_letters)
    r = randint(0, l - 2)
    return seed[:r] + seed[r + 1] + seed[r] + seed[r+2:]

def mutationC(seed: str)->str:
    """Insert a random byte"""
    l = len(seed)
    if (l <= 0):
        return choice(string.ascii_letters)
    r = randint(0, l - 1)
    return seed[:r] + choice(string.ascii_letters + string.digits) + seed[r:]

def mutationD(seed: str)->str:
    """Replace bytes with random values"""
    for i in range(randint(0, len(seed))):
        seed = mutationC(mutationA(seed))
    return seed

def mutationE(seed: str)->str:
    """Return a random length slice of the string from index 0"""
    if (len(seed) <= 0):
        return choice(string.ascii_letters)
    r = randint(0, len(seed) - 1)
    return seed[:r]

def mutationF(seed: str)->str:
    """Return a random length slice of the string from any index"""
    r = randint(0, len(seed) - 1)
    return seed[r:]

def mutationG(seed: str)->str:
    """Concatanate a string with itself"""
    return seed + seed

def mutationH(seed: str)->str:
    """Concatanate a string with its slice from index 0"""
    if (len(seed) <= 0):
        return choice(string.ascii_letters)
    r = randint(0, len(seed) - 1)
    return seed + seed[r:]  

def mutationI(seed: str)->str:
    """Replace a random character in a string with a random character"""
    l = choice(string.digits + string.ascii_letters)
    if (len(seed) <= 0):
        return choice(string.ascii_letters)
    r = randint(0, len(seed) - 1)
    return seed.replace(seed[r], l)

class Mutations():
    def __init__(self):
        self.successfullMutations = set()
        self.MUTATIONS_LIST = [mutationA,
             mutationB,
             mutationC,
             mutationD,
             mutationE,
             mutationF,
             mutationG,
             mutationH,
             mutationI
             ]

    def update_mutations(self, mutation):
        """Adds mutation function  to set of successful mutation
           which allows mutation functions that have yielded increased
           coverage or failure runs to be used more often

        Args:
            mutation (function): function to add
        """
        self.successfullMutations.add(mutation)
        
    def select_mutation_function(self):
        """Selects then next mutation function to use:
            if the set of cached mutation functions is non-empty, that means
            that we have some mutation functions that should be given more preference 
            and we select from that,
            otherwise we select a random mutation function

        Returns:
            function: mutation function to run next
        """
        if len(self.successfullMutations) > 0:
            return self.successfullMutations.pop()
        else:
            return choice(self.MUTATIONS_LIST)
