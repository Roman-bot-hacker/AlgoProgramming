from hamster_manager import HamsterManager
from in_out_manager import InOutManager


if __name__ == '__main__':
    InOutManager.read_data_from_file()
    print(InOutManager.array)
    InOutManager.array.sort()
    manager = HamsterManager(InOutManager.stock)
    print(manager.hmstr_choose(InOutManager.array))
    print(len(manager.choosen))
    print('\n\n\n')
    manager.hmstr_half(InOutManager.array, len(InOutManager.array)-1, 0)