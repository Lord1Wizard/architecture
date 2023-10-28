import random
from CakeGenerator import CakeGenerator
from GemGenerator import GemGenerator
from GoldGenerator import GoldGenerator

if __name__ == '__main__':
    fabricList = [GoldGenerator(), GemGenerator(), CakeGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()
