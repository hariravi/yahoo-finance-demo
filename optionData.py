from yahoo_fin import options
import pandas as pd
import sys

if __name__ == '__main__':
	STOCK = sys.argv[1]
	with pd.ExcelWriter(STOCK+".xlsx") as writer:  
		for date in options.get_expiration_dates(STOCK):
			options_at_expiry = options.get_options_chain(STOCK, date)
			options_at_expiry["calls"].to_excel(writer, sheet_name=date + " calls")
			options_at_expiry["puts"].to_excel(writer, sheet_name=date + " puts")
