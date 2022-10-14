from files_handler import FileHandler
from bs_handler import driver_test
from consts import default_input_file, default_output_file


def run(keyword, input_file=default_input_file, output_file=default_output_file):
    file_handler = FileHandler(input_file=input_file, output_file=output_file)
    file_handler.add_column(keyword=keyword)
    file_handler.export_to_csv(output_file)
    file_handler.export_to_csv(input_file)

# def test(keyword, input_file=default_input_file, output_file=default_output_file):
#     file_handler = FileHandler(input_file=input_file, output_file=output_file)
#     print(file_handler.html_test())


if __name__ == '__main__':
    run(keyword='SIC Code')
