from hamster_manager import HamsterManager
from in_out_manager import InOutManager


if __name__ == '__main__':
    InOutManager.read_data_from_file()
    print(InOutManager.array)
    InOutManager.array.sort()
    manager = HamsterManager(InOutManager.stock)
    print(manager.hmstr_choose(InOutManager.array))
    print(len(manager.choosen))