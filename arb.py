from fetch import *
from one_inch_fetch import *


def arb():
	exchange_rate = getExchangeRate(WETH, USDC)
	one_inch_exchange_rate = fetch(USDC, WETH, ethereum)

	#compare the exchange rate and find the arb opportunity

	print(f"0x: {exchange_rate}, 1inch: {one_inch_exchange_rate}")


arb()

