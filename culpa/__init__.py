import pandas as pd
import xlrd

__version__ = '1.0.0'

def read_col(fname, col):
    df = pd.read_excel(fname)
    return [str(x) for x in list(df[col])]

def read_file(fname):
    df = pd.read_excel(fname)
    return sorted([str(x) for x in list(df.columns)])

def main():
    from sys import argv
    if not 2 <= len(argv) <= 3:
        exit('Usage: culpa fname.xls [col]')
    if len(argv) == 2:
        print('\n'.join(read_file(argv[1])))
    if len(argv) == 3:
        print('\n'.join(read_col(argv[1], argv[2])))

if __name__ == '__main__':
    main()
