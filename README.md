# yahoo-finance-demo
Very basic python demo using yahoo finance module

File: optionData.py
Description: a very basic example of using the yahoo finance module in python, in this script I just save all future option data, including strike price, volatility, etc.

Usage: in the terminal, type
python optionData.py tsla
(Or insert any stock in the place of tsla)

The output of this code will be an excel (which will be formed in the same directory in which you execute the script), with sheets for each expiry date (corresponding to calls or puts on that day).

Prerequisites:
You need to install a few python libraries, you can do so using pip. To install pip on a mac, in the terminal, type:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
And then run the following commands: pip install yahoo_fin
pip install lxml
pip install requests-html
pip install openpyxl
(and maybe more, depending on what python libraries your computer has)
