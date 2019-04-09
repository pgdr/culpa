import pandas as pd
import xlrd

def main(fname):
    df = pd.read_excel(fname)
    return [str(x) for x in list(df.columns)]

if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        exit('Usage: app arg')
    print('\n'.join(main(argv[1])))
