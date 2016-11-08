# Overview

This is a stock_quote generate command line python script that generates the stock value of a stock based on the TICKER. It can also give you a 52 week min or a 52 week max. 

#### Usage Screen

```
$ ./stock_quote.py --help
usage: stock_quote.py [-h] [--version] ticker
you may not enter 2 separate arguments together.
ie --help GOOG will return an error
stock_quote - A tool for generating code coverage reports.

positional arguments:
  ticker           Stock ticker.
  ticker max52     52 Week Max.
  ticker min52     52 Week Min.
  i.e: GOOG min52
  
optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

