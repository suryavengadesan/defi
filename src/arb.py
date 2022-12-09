from fetch import *
from one_inch_fetch import *
from constants import *


def arb(fromToken, toToken, source, limit):
	# 
	# Step 1: 0x ETH/USDC get the bid price 
	#					buy toToken at 1inch
	# Step 2: 1inch WETH -> USDC
	#					sell toToken at 0x
	# print(f"arb fromToken: {address_currency_dict[fromToken]} toToken {address_currency_dict[toToken]}")
	bidRate = getBidRate(toToken, fromToken)["exchange_rate"]
	orders = fetch(toToken, fromToken, source, limit)

	# print(orders)
	arb_count = 0
	total_profit = 0
	total_cost = 0 
	#compare the exchange rate and find the arb opportunity
	for order in orders:
		if bidRate * (1 - transaction_cost) - order * (1 + transaction_cost) > 0:
			arb_count += 1
			total_profit += bidRate * (1 - transaction_cost) - order * (1 + transaction_cost)
			total_cost += order * (1 + transaction_cost)

	arb_opportunity = float(arb_count) / len(orders)
	profit_rate = float(total_profit) / total_cost if total_cost > 0 else 0

	# print(f"0x bid rate: {bidRate}, 1inch count: {len(orders)}")
	print(f"arb_count: {arb_count}, arb_opportunity: {arb_opportunity}, profit_rate: {profit_rate}")

	return arb_count, len(orders), arb_opportunity, profit_rate

def main():
	### WETH
	arb(WETH, USDC, ethereum, limit)
	arb(WETH, USDT, ethereum, limit)
	arb(WETH, DAI, ethereum, limit)
	# arb(WETH, WBTC, ethereum, limit)
	arb(WETH, BNB, ethereum, limit)
	# arb(WETH, MATIC, ethereum, limit)
	# arb(WETH, SHIBA, ethereum, limit)

	### WBTC
	arb(WBTC, USDC, ethereum, limit)
	# arb(WBTC, USDT, ethereum, limit)
	# arb(WBTC, DAI, ethereum, limit)
	# arb(WBTC, WETH, ethereum, limit)
	arb(WBTC, BNB, ethereum, limit)
	# arb(WBTC, MATIC, ethereum, limit)
	# arb(WBTC, SHIBA, ethereum, limit)

	### BNB
	arb(BNB, USDC, ethereum, limit)
	arb(BNB, USDT, ethereum, limit)
	# arb(BNB, DAI, ethereum, limit)
	arb(BNB, WETH, ethereum, limit)
	# arb(BNB, WBTC, ethereum, limit)
	# arb(BNB, MATIC, ethereum, limit)
	# arb(BNB, SHIBA, ethereum, limit)

	### MATIC
	arb(MATIC, USDC, ethereum, limit)
	# arb(MATIC, USDT, ethereum, limit)
	# arb(MATIC, DAI, ethereum, limit)
	# arb(MATIC, WETH, ethereum, limit)
	# arb(MATIC, WBTC, ethereum, limit)
	# arb(MATIC, BNB, ethereum, limit)
	# arb(MATIC, SHIBA, ethereum, limit)

	### SHIBA
	arb(SHIBA, USDC, ethereum, limit)
	# arb(SHIBA, USDT, ethereum, limit)
	# arb(SHIBA, DAI, ethereum, limit)
	# arb(SHIBA, WETH, ethereum, limit)
	# arb(SHIBA, WBTC, ethereum, limit)
	# arb(SHIBA, BNB, ethereum, limit)
	# arb(SHIBA, MATIC, ethereum, limit)

	### USDC
	# arb(USDC, USDT, ethereum, limit)
	# arb(USDC, DAI, ethereum, limit)
	arb(USDC, WETH, ethereum, limit)
	arb(USDC, WBTC, ethereum, limit)
	arb(USDC, BNB, ethereum, limit)
	# arb(USDC, MATIC, ethereum, limit)
	arb(USDC, SHIBA, ethereum, limit)

	### USDT
	arb(USDT, USDC, ethereum, limit)
	# arb(USDT, DAI, ethereum, limit)
	# arb(USDT, WETH, ethereum, limit)
	# arb(USDT, WBTC, ethereum, limit)
	arb(USDT, BNB, ethereum, limit)
	# arb(USDT, MATIC, ethereum, limit)
	# arb(USDT, SHIBA, ethereum, limit)

	### DAI
	arb(DAI, USDC, ethereum, limit)
	# arb(DAI, USDT, ethereum, limit)
	# arb(DAI, WETH, ethereum, limit)
	# arb(DAI, WBTC, ethereum, limit)
	arb(DAI, BNB, ethereum, limit)
	# arb(DAI, MATIC, ethereum, limit)
	# arb(DAI, SHIBA, ethereum, limit)




if __name__ == '__main__':
	main()
