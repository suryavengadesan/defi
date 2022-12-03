from fetch import *
from one_inch_fetch import *
from constants import *


def arb():
	# 
	# Step 1: 0x ETH/USDC get the bid price 
	# Step 2: 1inch USDC -> ETH
	bidRate = getBidRate(WETH, USDC)["exchange_rate"]
	orders = fetch(USDC, WETH, ethereum, limit)

	arb_count = 0 
	#compare the exchange rate and find the arb opportunity
	for order in orders:
		 if bidRate * (1 - transaction_cost) - order * (1 + transaction_cost) > 0:
		 	arb_count += 1

	arb_opportunity = float(arb_count) / limit

	print(f"0x bid rate: {bidRate}, 1inch: {orders}")
	print(f"arb_opportunity: {arb_opportunity}")

	return arb_opportunity

	
arb()

