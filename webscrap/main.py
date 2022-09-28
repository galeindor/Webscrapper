from files_handler import FileHandler


if __name__ == '__main__':

    info_file = "Stock_Screener.csv"
    file_handler = FileHandler(info_file)
    file_handler.add_market_cap()
    file_handler.export_to_csv(info_file)

