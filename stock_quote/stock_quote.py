import json
import urllib.request
import sys


def main():
    arguments = sys.argv
    if "stock_quote.py" in arguments:
        arguments.remove("stock_quote.py")
    if len(arguments) == 0:
        print("Please enter an argument")
    elif len(arguments) == 1:
        if arguments[0] == "-h" or arguments[0] == "--help":
            help()
        elif arguments[0] == "--version":
            print("version")
        else:
            url = convert_url(arguments[0]) 
            data = conv_json(url)
            if is_valid(data):
                ticker_data = json.loads(data)
                close_val = last_day(ticker_data)
                print(close_val)
            else:
                print("Invalid Argument/Ticker")
    
    elif len(arguments) == 2:
        url = convert_url(arguments[0]) 
        data = conv_json(url)
        if is_valid(data):
            ticker_data = json.loads(data)
            if arguments[1].upper() == "MAX52":
                print(max_52(ticker_data))
            elif arguments[1].upper() == "MIN52":
                print(min_52(ticker_data))
        else:
            print("Invalid Argument/Ticker")
    else:
        print("Invalid Argument/Ticker. Type --help for help")
        
            
        
def is_valid(ticker):
    try:
        json_object = json.loads(ticker)
    except ValueError as e:
        return False
    return True

def convert_url(ticker):
    base = "http://chartapi.finance.yahoo.com/instrument/1.0/"
    suffix = "/chartdata;type=quote;range=1y/json"
    url = base+ticker.upper()+suffix
    return url

def last_day(ticker_data):
    return ticker_data["series"][len(ticker_data["series"])-1]['close']

    '''
    conv_json gets the data from the URL and truncates it to convert it JSON.
    '''

def help():
    return "usage: stock_quote.py [-h] [--version] ticker", \
        "stock_quote - A tool for generating code coverage reports.", \
        "positional arguments:", \
        "ticker      Stock ticker.", \
        "optional arguments:", \
        " -h, --help  show this help message and exit", \
        "--version   show program's version number and exit"

def max_52(ticker_data):
    max_val = -sys.maxsize
    for x in range(len(ticker_data["series"])):
        max_val = max(ticker_data["series"][x]['close'],max_val)
    return max_val

def min_52(ticker_data):
    min_val = sys.maxsize
    for x in range(len(ticker_data["series"])):
        min_val = min(ticker_data["series"][x]['close'],min_val)
    return min_val

def conv_json(url):
    
    '''
    Yahoo does not return JSON Formatted output. The output is truncated to make sure it is JSON.
    '''
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data[29:-1]
    
if __name__ == '__main__':
    main()




