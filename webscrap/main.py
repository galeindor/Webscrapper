from files_handler import FileHandler
from bs_handler import driver_test
from consts import default_input_file, default_output_file
import ptb

ptb.enable()


def run(keyword, input_file=default_input_file, output_file=default_output_file, force_update=False):
    file_handler = FileHandler(input_file=input_file, output_file=output_file)
    file_handler.add_column(keyword=keyword, force_update=force_update)
    file_handler.export_to_csv(output_file)


if __name__ == '__main__':
    run(keyword='Market Cap', force_update=True)
