from input_output_manager import InOutManager
from graph import Graph

if __name__ == '__main__':
    in_out_manager = InOutManager()
    in_out_manager.read_data_from_file()
    graph = Graph(in_out_manager.graph)
    graph.width_search()
    in_out_manager.write_data_to_file(graph.get_most_active_student())
