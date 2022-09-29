from files_handler import FileHandler
import consts

if __name__ == '__main__':
    file_handler = FileHandler(input_file=consts.input_file_name , output_file= consts.output_file_name)
    file_handler.add_market_cap()
    file_handler.export_to_csv(consts.output_file_name)

