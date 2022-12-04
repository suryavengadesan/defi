# https://docs.1inch.io/docs/limit-order-protocol/api
# https://docs.1inch.io/docs/limit-order-protocol/guide/limit-order-structure

import requests
import json
from constants import *

def fetch(makerAsset, takerAsset, source=1, limit=10):
	"""

	"""
	ethplorerKey = "EK-w5S5E-dZCXjb9-uSqWJ"
	quoteTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=makerAsset, key=ethplorerKey)
	r = requests.get(url = quoteTokenURL)
	data = r.json()
	makerDecimals = int(data["decimals"])
	baseTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=takerAsset, key=ethplorerKey)
	r = requests.get(url = baseTokenURL)
	data = r.json()
	takerDecimals = int(data["decimals"])
	
	# print(f"taker decimals: {takerDecimals} and make decimals: {makerDecimals}")

	URL = f"https://limit-orders.1inch.io/v2.0/{source}/limit-order/all?page=1&limit={limit}&statuses=%5B1%5D&takerAsset={takerAsset}&makerAsset={makerAsset}"
	# print(URL)
	r = requests.get(url = URL)

	exchanges = json.loads(r.content)
	
	# print(json.dumps(exchanges, indent=4))

	orders = []
	for exchange in exchanges:
		exchange_rate = float(exchange["makerRate"]) * 10**(makerDecimals - takerDecimals)
		# output = {"from":fromToken, "to": toToken, "exchange_rate":exchange_rate} 
		# print(output)
		orders.append(exchange_rate)
		
	return orders

	


def main():
	# result = fetch(USDC, WETH, ethereum)
	result = fetch(USDC, WBTC, ethereum)
	# result = fetch(WETH, USDC, ethereum)
	# fetch(USDC, BNB, ethereum)
	# fetch(binance_PETH, binance_USDC, binance)
	#fetch(polygon_WBTC, polygon_USDC, polygon)
	# fetch(optimism_WBTC, optimism_USDC, optimism)

	print(result)

if __name__ == '__main__':
	main()