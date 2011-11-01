Basic programming-competency test problem.

Shamelessly ripped-off from David Beazley's training site:
http://www.dabeaz.com/chicago/preparation.html

-------------------------------------------------------------------------------
Suppose the file portfolio.dat contains information about some stocks that you
purchased. There are three columns showing the name, number of shares, and
purchase price.

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44

A different file, prices.dat, contains a list of current stock prices. The
columns in this file are the stock name and price.

GOOG 509.71
YHOO 28.34
IBM 106.11
MSFT 30.47
AAPL 122.13
SUNW 5.01
AA 39.91
CAT 78.58
GE 37.38
HPQ 38.15

Write a program that reads the stock portfolio in portfolio.dat, the stock
prices from prices.dat, and prints out how much the entire portfolio has
increased or decreased in value.
-------------------------------------------------------------------------------

EXTRA CREDIT: 
-------------
Portfolio.dat and prices.dat both have a small number of stocks. At the
meetup, a second set of files will have a much larger number of stocks to
analyze. We'll use the comparison between both sizes to talk about writing
code that is reusable and that scales to handle a larger number of inputs. 
