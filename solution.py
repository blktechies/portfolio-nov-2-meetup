#!/usr/bin/env python

import os

from decimal import Decimal


PATH_FILE__PORTFOLIO = os.path.join('data', 'portfolio.dat')
PATH_FILE__PRICES = os.path.join('data', 'prices.dat')


def main():
    portfolio = {}
    prices = {}
    initial_cost = 0
    final_value = 0

    # Read purchasing data,
    # extracting portfolio items and accumulating shares and total cost
    for line in open(PATH_FILE__PORTFOLIO):
        line = line.split()
        stock = line[0]
        shares = int(line[1])
        price = Decimal(line[2])
        portfolio[stock] = portfolio.get(stock, 0) + shares
        initial_cost += price * shares

    # Read and extract current price data
    for line in open(PATH_FILE__PRICES):
        line = line.split()
        stock = line[0]
        price = Decimal(line[1])
        prices[stock] = price

    # Lookup current prices and accumulate total current value
    for stock, shares in portfolio.items():
        price = prices[stock]
        value = price * shares
        final_value += value

    print "INITIAL COST: \t", initial_cost
    print "FINAL VALUE: \t", final_value
    print "-"*25
    print "DIFFERENCE: \t", final_value - initial_cost


if __name__ == '__main__':
    main()
