import pandas as pd
from bs_handler import Soup
from consts import endings, EMPTY_CELL


class FileHandler:
    def __init__(self, input_file, output_file):
        self._bs = None
        self._data = pd.read_csv(input_file, index_col=None)
        self._out_file = output_file
        self._in_file = input_file

    # def html_test(self):
    #     self._bs = Soup('WVFC', 'Market Cap')
    #     return self._bs.get_value_test()

    def add_column(self, keyword):
        if keyword not in endings.keys():
            print(f'{keyword} is not a valid keyword , exiting')
            return
        errors_dict = {}
        if keyword not in self._data.columns:  # if column doesn't exist , create empty column
            self._data[keyword] = EMPTY_CELL
            self.export_to_csv(self._in_file)
            self.export_to_csv(self._out_file)
        symbol = None
        while True:
            keep_trying = False
            for index in range(len(self._data)):
                try:
                    symbol = self._data['Symbol'].loc[index]
                    value = self._data.loc[index, keyword]
                    if value == EMPTY_CELL:
                        if self._bs is None:
                            self._bs = Soup(symbol, keyword)
                        else:
                            self._bs.reset(symbol)
                        keep_trying = True
                    else:
                        continue
                    self._data.loc[index, keyword] = self._bs.locate_keyword(symbol)
                    self.export_to_csv(self._out_file)
                except Exception as e:
                    errors_dict[symbol] = e
            print('finished run with the following errors:')
            for error in errors_dict:
                print(f'{error} got {errors_dict[error]}')
            print(f'number of errors: {len(errors_dict)}')
            if not keep_trying:
                return
            self.export_to_csv(self._in_file)
            print('-------RESTART RUN-------')

    def export_to_csv(self, file_name=None):
        if file_name is None:
            file_name = self._out_file
        self._data.to_csv(file_name, index=False)
