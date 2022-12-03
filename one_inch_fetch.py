# https://docs.1inch.io/docs/limit-order-protocol/api
# https://docs.1inch.io/docs/limit-order-protocol/guide/limit-order-structure

import requests
import json
from contants import *

def fetch(takerAsset, makerAsset, source=1, limit=10):
	"""

	"""
	URL = f"https://limit-orders.1inch.io/v2.0/{source}/limit-order/all?page=1&limit={limit}&statuses=%5B1%2C2%2C3%5D&takerAsset={takerAsset}&makerAsset={makerAsset}"
	# print(URL)
	r = requests.get(url = URL)

	exchanges = json.loads(r.content)
	for exchange in exchanges:
		fromToken = address_currency_dict[exchange["data"]["makerAsset"]]
		toToken = address_currency_dict[exchange["data"]["takerAsset"]]
		exchange_rate = exchange["makerRate"]
		output = {"1inch - from":fromToken, "to": toToken,"exchange_rate":exchange_rate * 1000000000000} 
		print(output)

	# print(json.dumps(data, indent=4))


def main():
	fetch(USDC, WETH, ethereum)
	# fetch(binance_PETH, binance_USDC, binance)
	#fetch(polygon_WBTC, polygon_USDC, polygon)
	# fetch(optimism_WBTC, optimism_USDC, optimism)

if __name__ == '__main__':
	main()