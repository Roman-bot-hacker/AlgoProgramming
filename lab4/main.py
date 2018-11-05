from input_output_manager import InOutManager
from graph import Graph

if __name__ == '__main__':
    in_out_manager = InOutManager()
    graph = Graph(in_out_manager.read_data_from_file())
    in_out_manager.write_data_to_file(graph.search_most_active_student())
