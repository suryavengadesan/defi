# Address

## ETH
WBTC = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
USDT = "0xdac17f958d2ee523a2206206994597c13d831ec7"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
USDC = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
BNB = "0xb8c77482e45f1f44de1745f52c74426c631bdd52"
MATIC = "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0"
DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
SHIBA = "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"

## Binance
binance_USDC = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"
binance_PETH = "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"

## Polygon
polygon_USDT = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
polygon_USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
polygon_WBTC = "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6"

## Optimism
optimism_USDT = "0x94b008aA00579c1307B0EF2c499aD98a8ce58e58"
optimism_USDC = "0x7F5c764cBc14f9669B88837ca1490cCa17c31607"
optimism_WBTC = "0x68f180fcCe6836688e9084f035309E29Bf0A2095"

# 1inch source id
ethereum = 1
binance = 56
polygon = 137
optimism = 10

# Address mapping
address_currency_dict = {
	'0x2260fac5e5542a773aa44fbcfedf7c193bc2c599': 'WBTC',
	'0xdac17f958d2ee523a2206206994597c13d831ec7': 'USDT',
	'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2': 'WETH',
	'0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48': 'USDC',
	"0xb8c77482e45f1f44de1745f52c74426c631bdd52": 'BNB',
	"0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0": 'MATIC',
	"0x6b175474e89094c44da98b954eedeac495271d0f": 'DAI',
	"0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce": 'SHIBA'
}

# Transaction cost
transaction_cost = 0.02

# Order limit number
limit = 500