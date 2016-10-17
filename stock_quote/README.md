# Overview

Much of what we do at Airware involves writing custom software to automate
processes.  This software often interacts with the APIs of other tools.  This
task will demonstrate how you approach designing software and your experience
interacting with APIs.

# Problem statement

Write a command line tool to retrieve the current price of a given stock. The
tool should accept the stock ticker as an argument.

Bonuses:

* Write a Markdown README.md with usage instructions.
* Design to be able to easily switch between retrieving quotes from Google
Finance and Yahoo! Finance.
* Retrieve the 52 week high
* Retrieve the 52 week low
* Implement a basic unit test

### Example APIs

Since the point of this exercise not to research stock quotes, but rather
implement at tool, here are APIs that you can use as a starting point.

* http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=1y/json
* http://finance.google.com/finance/info?client=ig&q=NASDAQ:GOOG

# Requirements

* Write it it Python or GoLang.  If there is a good reason to write in another
language, please explain your choice.  No bash.
* It must run.  Comment out troublesome code to ensure it runs if you run out of
 time.
* There must be a help / usage menu.

# Example Output:

#### Usage Screen

```
$ ./stock_quote.py --help
usage: stock_quote.py [-h] [--version] ticker

stock_quote - A tool for generating code coverage reports.

positional arguments:
  ticker      Stock ticker.

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

#### Example Output

```
$ ./stock_quote.py GOOG
558.32
```
