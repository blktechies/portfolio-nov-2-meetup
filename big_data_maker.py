#!/usr/bin/env python


import os
import string

from random import choice


PATH_FILE__BIG_PORTFOLIO = os.path.join('data', 'big-portfolio.dat')
PATH_FILE__BIG_PRICES = os.path.join('data', 'big-prices.dat')

# 10 gigs is probably sufficient to not fit in most people's personal
# computer's RAM
TARGET_FILE_SIZE = 10 * (1024**3)

# In actuality there're roughly 2.5k listings on NYSE:
# http://en.wikipedia.org/wiki/New_York_Stock_Exchange
MAX_STOCKS = 5000

CHAR_POOL = string.uppercase
DIG_POOL = string.digits
LEN_POOL = (1, 2, 3)


def random_stock():
    return ''.join([choice(CHAR_POOL) for i in xrange(3)])


def random_price():
    dollars = ''.join([choice(DIG_POOL) for i in xrange(choice(LEN_POOL))])
    cents = ''.join([choice(DIG_POOL) for i in xrange(2)])
    price = '{0}.{1}'.format(dollars, cents)
    return price


def random_shares():
    return ''.join([choice(DIG_POOL) for i in xrange(choice(LEN_POOL))])


def main():
    # Make a set of stocks
    stocks = list(set([random_stock() for s in xrange(MAX_STOCKS)]))

    # Pick and write current prices for our set of stocks
    current_prices = ['{0} {1}\n'.format(s, random_price()) for s in stocks]
    with open(PATH_FILE__BIG_PRICES, 'wb') as prices_file:
        prices_file.writelines(current_prices)

    # Generate a big trade log
    with open(PATH_FILE__BIG_PORTFOLIO, 'wb') as big_log_file:
        while os.stat(PATH_FILE__BIG_PORTFOLIO).st_size < TARGET_FILE_SIZE:
            stock = choice(stocks)
            shares = random_shares()
            price = random_price()

            record = '{0} {1} {2}\n'.format(stock, shares, price)
            big_log_file.write(record)


if __name__ == '__main__':
    main()
