from electro_manager import *
from input_output_manager import InOutManager

if __name__ == '__main__':
    in_out_manager = InOutManager()
    in_out_manager.read_data_from_file()
    in_out_manager.write_data_to_file(
        find_max_length(in_out_manager.distance,
                        in_out_manager.max_heights))