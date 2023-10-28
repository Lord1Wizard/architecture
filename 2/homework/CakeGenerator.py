from ItemFabric import ItemFabric
from CakeReward import CakeReward


class CakeGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук с тортом")
        return CakeReward()
