import numpy as np
import pandas as pd
from bs_handler import Soup


class FileHandler:
    def __init__(self, file_name):
        self._bs = None
        self._data = pd.read_csv(file_name)
        self._output_file_name = file_name

    def add_market_cap(self):
        counter = 0
        for index in range(5):
            try:
                symbol = self._data['Symbol'].loc[index]
                self._bs = Soup(symbol)
                self._data.loc[index, 'Market Cap'] = self._bs.locate_market_cap()
                counter+=1
                if counter > 50:
                    self.export_to_csv(self._output_file_name)

            except Exception as e:
                print(f"got execption for symbol: {symbol} \nexecption: {e}")

    def export_to_csv(self, file_name):
        self._data.to_csv(file_name)

