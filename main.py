import os
import numpy as np
import pandas as pd

from functions.read_convert_sheet import read_convert_sheet
from functions.format_stations import format_stations


def main():
    file_name = 'teste'
    cwd = os.getcwd()
    path_sheet = f'{cwd}/{file_name}.xlsx'

    converted_sheet = read_convert_sheet(path_sheet)
    print(format_stations(converted_sheet)[5])


if __name__ == '__main__':
    main()