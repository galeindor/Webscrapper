from files_handler import FileHandler
from bs_handler import driver_test
from consts import input_file_name,output_file_name
if __name__ == '__main__':
    file_handler = FileHandler(input_file=input_file_name, output_file=output_file_name)
    file_handler.add_column(keyword='Market Cap')
    file_handler.export_to_csv(output_file_name)
    file_handler.export_to_csv(input_file_name)

