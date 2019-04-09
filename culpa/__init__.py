import pandas as pd
import xlrd

def read_col(fname, col):
    df = pd.read_excel(fname)
    return [str(x) for x in list(df[col])]

def main(fname):
    df = pd.read_excel(fname)
    return [str(x) for x in list(df.columns)]

if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        exit('Usage: app arg')
    if len(argv) == 2:
        print('\n'.join(main(argv[1])))
    if len(argv) == 3:
        print('\n'.join(read_col(argv[1], argv[2])))
