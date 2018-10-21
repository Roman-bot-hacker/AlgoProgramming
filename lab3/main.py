from in_out_manager import InOutManager
from DFS import DFS

if __name__ == '__main__':
    InOutManager.read_data_from_file()
    dfs_manager = DFS()
    dfs_manager.depth_first_order(InOutManager.graph)
    InOutManager.write_data_to_file(dfs_manager.get_reverse_post())