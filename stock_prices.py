def get_stock_profit(stock_prices_yesterday):
	if len(stock_prices_yesterday) < 2:
		raise IndexError('more than 2 is required')
	min_price = stock_prices_yesterday[0]
	max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	
	for time, curr_price in enumerate (stock_prices_yesterday):
		# enumerate to avoid using  -- > for i in range(List) 
											#item = List[i]
		# there has to be two entries atleast for buy and sell 
		if time == 0:
			continue  
		#print ("iterator - " + str(time))
		potential_profit = curr_price - min_price
		min_price = min (curr_price, min_price)
		max_profit = max (potential_profit, max_profit)
	return max_profit
		
#stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [10]
print("Maximum_profit - "+ str(get_stock_profit(stock_prices_yesterday)))