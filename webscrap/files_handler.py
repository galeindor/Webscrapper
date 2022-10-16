import pandas as pd
from bs_handler import Soup
from consts import endings, EMPTY_CELL


class FileHandler:
    def __init__(self, input_file, output_file):
        self._bs = None
        self._input_data = pd.read_csv(input_file, index_col=None)
        try:
            self._output_data = pd.read_csv(output_file, index_col=None)
        except FileNotFoundError:
            self._output_data = self._input_data
        self._out_file = output_file
        self._in_file = input_file

    def add_column(self, keyword, force_update):
        if keyword not in endings.keys():
            print(f'{keyword} is not a valid keyword , exiting')
            return
        errors_dict = {}
        if keyword not in self._input_data.columns:  # if column doesn't exist , create empty column
            self._input_data[keyword] = EMPTY_CELL
            self._output_data[keyword] = EMPTY_CELL
            self.export_to_csv(self._in_file)
            self.export_to_csv(self._out_file)
        symbol = None
        for index in range(len(self._input_data)):
            try:
                symbol = self._input_data['Symbol'].loc[index]
                value = self._output_data.loc[index, keyword]
                if value == EMPTY_CELL or force_update:
                    if self._bs is None:
                        self._bs = Soup(symbol, keyword)
                    else:
                        self._bs.reset(symbol)
                else:
                    continue

                self._output_data.loc[index, keyword] = self._bs.locate_keyword(symbol, keyword)
                self.export_to_csv(self._out_file)
            except Exception as e:
                errors_dict[symbol] = e
        print('finished run with the following errors:')
        for error in errors_dict:
            print(f'{error} got {errors_dict[error]}')
        print(f'number of errors: {len(errors_dict)}')

    def export_to_csv(self, file_name=None):
        if file_name is None:
            file_name = self._out_file
        self._output_data.to_csv(file_name, index=False)
