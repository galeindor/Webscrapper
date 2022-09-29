import pandas as pd
from bs_handler import Soup


class FileHandler:
    def __init__(self, input_file, output_file):
        self._bs = None
        self._data = pd.read_csv(input_file)
        self._out_file = output_file

    def add_market_cap(self):
        symbol = ''
        for index in range(len(self._data)):
            try:
                symbol = self._data['Symbol'].loc[index]
                market_cap = self._data.loc[index, 'Market Cap']
                if market_cap == ' ' or market_cap is None:
                    self._bs = Soup(symbol)
                else:
                    continue
                self._data.loc[index, 'Market Cap'] = self._bs.locate_market_cap()
                self.export_to_csv()

            except Exception as e:
                print(f"got execption for symbol: {symbol} \n{e}")

    def export_to_csv(self, file_name=None):
        if file_name is None:
            file_name = self._out_file
        self._data.to_csv(file_name)

