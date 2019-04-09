import pandas as pd
import xlrd

def main(fname):
    df = pd.read_excel(fname)
    return df.columns

if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        exit('Usage: app arg')
    print(main(argv[1]))
