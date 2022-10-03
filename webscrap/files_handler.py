import pandas as pd
from bs_handler import Soup
from consts import endings


class FileHandler:
    def __init__(self, input_file, output_file):
        self._bs = None
        self._data = pd.read_csv(input_file)
        self._out_file = output_file
        self._in_file = input_file

    def add_column(self, keyword):
        assert keyword not in endings.items()

        if keyword not in self._data.columns:  # if column doesn't exist , create empty column
            self._data[keyword] = None
            self._data.to_csv(self._in_file)
        symbol = None
        for index in range(len(self._data)):
            try:
                symbol = self._data['Symbol'].loc[index]
                value = self._data.loc[index, keyword]
                if value == ' ' or value is None:
                    if self._bs is None:
                        self._bs = Soup(symbol, keyword)
                    else:
                        self._bs.reset(symbol)
                else:
                    continue
                self._data.loc[index, keyword] = self._bs.locate_keyword(symbol)
                self.export_to_csv()

            except Exception as e:
                print(f"got execption for symbol: {symbol} \n{e}")

    def export_to_csv(self, file_name=None):
        if file_name is None:
            file_name = self._out_file
        self._data.to_csv(file_name)
