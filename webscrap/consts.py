endings = {
    'Market Cap': 'security',
    'SIC Code': 'profile',
    'Description': 'profile'
}

# each
class_names = {
    'Market Cap': {
        'outer_index': 0, 'inner_index': 0, 'outer': '_8AXJn4ourf sc-htpNat jtWIOA sc-bdVaJa gRrvFh',
        'inner': 'sc-bdVaJa kYmYWE'
    },
    'SIC Code': {
        'outer_index': 0, 'inner_index': 0, 'outer': 'B9e-1byHTk n6L6mBS6Y- _36meAm2WWk',
        'inner': '_383TUBEH9m sc-bdVaJa iHZvIS'
    },
    'Description': {
        'outer_index': 0, 'inner_index': 0, 'outer': '_2Ff6O56evM sc-bdVaJa dmWroL', 'inner': '_3qFD1hZwGn'
    }
}
default_input_file = 'Stock_input.csv'
default_output_file = 'Stock_output.csv'
EMPTY_CELL = '.'
SLEEP_TIME = 5

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}
test_symbols = ['ADMT',
                "ACMT", "ACMTA", "WHEN", "AGDY", "SPQS", "RGRX", "ALTX", "ABCP", "ABMC", 'ARTM', 'AVOT', 'CFNB', 'ANDR',
                'SYQH',
                'MICR', 'ARTNB', 'ATROB', 'AMNL', 'AIFS',
                'BBBK',
                'BISA',
                'BKUT', 'BRBW', 'BHRB',
                'BURCA', 'BZYR', 'BUKS', 'CAWW', 'CCFN', 'CPTP', 'CPKF', 'CBAF', 'CZBT', 'CIWV', 'CEFC', 'CNAF', 'CMTV',
                'CNGA', 'ACFN', 'DBRM', 'DIMC', 'ELST', 'ETCC', 'ENZN', 'ENBP', 'DHCC', 'EXSR', 'FFWC', 'FIDS', 'FMBL',
                'FABP', 'FSCR', 'FETM', 'FBSI', 'FBTT', 'FCNCB', 'FCIC', 'FKYS', 'FBAK',
                'ELMA',
                'FINN', 'FLEW', 'HCBN', 'HMLN', 'HFBK', 'HBSI', 'HONT',
                'WGEI',
                'INRD', 'ITDN',
                'IVRO',
                'JBTC', 'JUVF',
                'KISB', 'LPHM', 'LINS', 'LINSA', 'LYBC', 'MLGF',
                'MNBP', 'MCHT', 'PSSR', 'MNPP', 'MBKL', 'MTRT', 'MPAD', 'MMTRS', 'MUEL'
                ]

