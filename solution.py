#!/usr/bin/env python


from decimal import Decimal


portfolio = open('data/portfolio.dat', 'r').readlines()
stockcost = []
sharesdict = {}

for line in portfolio:
	stock,shares,price = line.split( )
    # This adds the share count if the same stock is purchased on more than one
    # occasion
	sharesdict.setdefault(stock, 0)
	sharesdict[stock] += Decimal(shares)

stockinfo = (line.split() for line in portfolio)

for item in stockinfo:
	stockcost.append (Decimal(item[1])*Decimal(item[2]))

prices = open('data/prices.dat').readlines()
portfolio_cost = sum(stockcost)
stockvalue = []
pricedict = {}

for line in prices:
	stock,value = line.split( )
	pricedict[stock] = Decimal(value)

for k in pricedict:
	if k in sharesdict:
		stockvalue.append(sharesdict[k]*pricedict[k])

portfolio_value = sum(stockvalue)


print (portfolio_value) - (portfolio_cost)
