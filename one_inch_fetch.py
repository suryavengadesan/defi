# https://docs.1inch.io/docs/limit-order-protocol/api
# https://docs.1inch.io/docs/limit-order-protocol/guide/limit-order-structure

import requests
import json

ethereum = 1
eth_WBTC = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
eth_USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
eth_WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
eth_USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

binance = 56
binance_USDC = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"
binance_PETH = "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"

polygon = 137
polygon_USDT = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
polygon_USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
polygon_WBTC = "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6"

optimism = 10
optimism_USDT = "0x94b008aA00579c1307B0EF2c499aD98a8ce58e58"
optimism_USDC = "0x7F5c764cBc14f9669B88837ca1490cCa17c31607"
optimism_WBTC = "0x68f180fcCe6836688e9084f035309E29Bf0A2095"


def fetch(takerAsset, makerAsset, source=1, limit=10):
	"""

	"""
	URL = f"https://limit-orders.1inch.io/v2.0/{source}/limit-order/all?page=1&limit={limit}&statuses=%5B1%2C2%2C3%5D&takerAsset={takerAsset}&makerAsset={makerAsset}"
	print(URL)
	r = requests.get(url = URL)

	parsed_data = json.loads(r.content)
	print(json.dumps(parsed_data, indent=4))


def main():
	fetch(eth_WBTC, eth_USDC, ethereum)
	# fetch(binance_PETH, binance_USDC, binance)
	#fetch(polygon_WBTC, polygon_USDC, polygon)
	# fetch(optimism_WBTC, optimism_USDC, optimism)

if __name__ == '__main__':
	main()