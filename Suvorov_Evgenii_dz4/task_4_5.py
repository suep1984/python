import utils
import sys

if __name__ == '__main__':
    example_cur, example_date = utils.currency_rates(sys.argv[1])
    if len(sys.argv) == 2:
        print(f' {example_cur}, {example_date}')
    else:
        print(None)
