from files_handler import FileHandler
from bs_handler import driver_test
import consts

if __name__ == '__main__':
    file_handler = FileHandler(input_file=consts.input_file_name, output_file=consts.output_file_name)
    file_handler.add_column(keyword='Market Cap')
    file_handler.export_to_csv(consts.output_file_name)
