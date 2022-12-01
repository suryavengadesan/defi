# https://docs.0x.org/introduction/0x-concept-videos 
# https://www.geeksforgeeks.org/get-post-requests-using-python/
# https://docs.0x.org/0x-api-orderbook/api-references/get-orderbook-v1
# https://stackoverflow.com/questions/13142347/how-to-remove-leading-and-trailing-zeros-in-a-string-python
# {"from":"from_currency", "to": "to_currency","exchange_rate":<rate> } 
# https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API?from=etop#get-token-info

import requests

WBTC = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
testA = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
testB = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"

#baseToken = WETH 
#quoteToken = USDT 

#baseToken = USDT
#quoteToken = WETH 

baseToken = USDC
quoteToken = WETH 

#baseToken = testA
#quoteToken = testB 


tokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey=freekey"



URL = "https://api.0x.org/orderbook/v1?quoteToken={quote}&baseToken={base}&page=1&perPage=1".format(quote=quoteToken, base=baseToken)
#URL = "https://api.0x.org/sra/v4/orders?page=3&perPage=20"
r = requests.get(url = URL)
data = r.json()
fromToken = data["bids"]["records"][0]["order"]["makerToken"]
toToken = data["bids"]["records"][0]["order"]["takerToken"]
fromTokenAmountRaw = data["bids"]["records"][0]["order"]["makerAmount"]
fromTokenAmount = int(data["bids"]["records"][0]["order"]["makerAmount"].rstrip("0"))
toTokenAmountRaw = data["bids"]["records"][0]["order"]["takerAmount"].rstrip("0")
toTokenAmount = int(data["bids"]["records"][0]["order"]["takerAmount"].rstrip("0"))
exchangeRate = float(float(fromTokenAmount) / float(toTokenAmount))


print(fromToken)
print(toToken)
print(fromTokenAmountRaw)
print(fromTokenAmount)
print(toTokenAmountRaw)
print(toTokenAmount)
print(exchangeRate)
#print(data)
ethplorerKey = "EK-w5S5E-dZCXjb9-uSqWJ"
quoteTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=quoteToken, key=ethplorerKey)
#quoteTokenURL = "https://kovan-api.ethplorer.io/getTokenInfo/{token}?apiKey=freekey".format(token=quoteToken)


r = requests.get(url = quoteTokenURL)
data = r.json()
print("QUOTE")
#print(data)
print(data["decimals"])

def getBidRate(quoteToken, baseToken):
	'''
	Fetches only the first bid value
	takerToken is equal to baseToken
	'''
	ethplorerKey = "EK-w5S5E-dZCXjb9-uSqWJ"
	quoteTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=quoteToken, key=ethplorerKey)
	r = requests.get(url = quoteTokenURL)
	data = r.json()
	quoteDecimals = int(data["decimals"])
	baseTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=baseToken, key=ethplorerKey)
	r = requests.get(url = baseTokenURL)
	data = r.json()
	baseDecimals = int(data["decimals"])
	#print(quoteDecimals)
	#print(baseDecimals)


	URL = "https://api.0x.org/orderbook/v1?quoteToken={quote}&baseToken={base}&page=1&perPage=1".format(quote=quoteToken, base=baseToken)
	r = requests.get(url = URL)
	data = r.json()

	if (len(data["bids"]["records"]) == 0):
		return "NO BID AVAILABLE"

	fromToken = data["bids"]["records"][0]["order"]["makerToken"]
	toToken = data["bids"]["records"][0]["order"]["takerToken"]
	fromTokenAmount = int(data["bids"]["records"][0]["order"]["makerAmount"]) # "12312341200000000000000" ~ 1231.23412
	toTokenAmount = int(data["bids"]["records"][0]["order"]["takerAmount"])
	#print(fromTokenAmount)
	#print(toTokenAmount)
	fromTokenAmount = fromTokenAmount / (10 ** quoteDecimals)
	toTokenAmount = toTokenAmount / (10 ** baseDecimals)
	#print(fromTokenAmount)
	#print(toTokenAmount)
	exchangeRate = float(float(fromTokenAmount) / float(toTokenAmount))
	#print(fromTokenAmount/toTokenAmount)
	output = {"from":fromToken, "to": toToken,"exchange_rate":exchangeRate}
	return output

def getAskRate(quoteToken, baseToken):
	'''
	Fetches only the first ask value
	makerToken is equal to baseToken
	'''
	ethplorerKey = "EK-w5S5E-dZCXjb9-uSqWJ"
	quoteTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=quoteToken, key=ethplorerKey)
	r = requests.get(url = quoteTokenURL)
	data = r.json()
	quoteDecimals = int(data["decimals"])
	baseTokenURL = "https://api.ethplorer.io/getTokenInfo/{token}?apiKey={key}".format(token=baseToken, key=ethplorerKey)
	r = requests.get(url = baseTokenURL)
	data = r.json()
	baseDecimals = int(data["decimals"])
	#print(quoteDecimals)
	#print(baseDecimals)

	URL = "https://api.0x.org/orderbook/v1?quoteToken={quote}&baseToken={base}&page=1&perPage=1".format(quote=quoteToken, base=baseToken)
	r = requests.get(url = URL)
	data = r.json()
	if (len(data["asks"]["records"]) == 0):
		return "NO ASK AVAILABLE"

	fromToken = data["asks"]["records"][0]["order"]["makerToken"]
	toToken = data["asks"]["records"][0]["order"]["takerToken"]
	fromTokenAmount = int(data["asks"]["records"][0]["order"]["makerAmount"])#.rstrip("0"))
	toTokenAmount = int(data["asks"]["records"][0]["order"]["takerAmount"])#.rstrip("0"))
	#print(fromTokenAmount)
	#print(toTokenAmount)
	fromTokenAmount = fromTokenAmount / (10 ** baseDecimals)
	toTokenAmount = toTokenAmount / (10 ** quoteDecimals)
	#print(fromTokenAmount)
	#print(toTokenAmount)
	exchangeRate = float(float(fromTokenAmount) / float(toTokenAmount))
	#print(fromTokenAmount/toTokenAmount)
	output = {"from":fromToken, "to": toToken,"exchange_rate":exchangeRate}
	return output

def getExchangeRate(tokenA, tokenB):
	'''
	Value of tokenA in tokenB
	'''
	#print(getBidRate(USDC, WETH) == getAskRate(USDC, WETH))
	#print(getAskRate(tokenA, tokenB) == getBidRate(tokenB, tokenA))
	#return getAskRate(tokenA, tokenB)
	askRate = getAskRate(tokenA, tokenB)
	bidRate = getBidRate(tokenB, tokenA)
	if askRate == "NO ASK AVAILABLE" and bidRate == "NO BID AVAILABLE":
		return "NO EXCHANGE"
	elif askRate == "NO ASK AVAILABLE": 
		return bidRate
	else:
		return askRate
	

print(getExchangeRate(WETH, USDC))
print(getExchangeRate(USDC, WETH))
print(getExchangeRate(WBTC, USDC))
print(getExchangeRate(USDC, WBTC))
print(getExchangeRate(WBTC, WETH))
print(getExchangeRate(WETH, WBTC))
#print(getBidRate(WETH, USDC))
#print(getAskRate(WETH, USDC))
#print(getBidRate(USDC, WETH))
#print(getAskRate(USDC, WETH))
#print(getBidRate(USDC, WBTC))
#print(getAskRate(USDC, WBTC))

#convertAtoB

'''
Interactive orderbook (e.g. EtherDelta, Binance)
https://www.binance.com/en/orderbook/ETH_USDT
'''

'''
Order Book APIS
https://docs.cryptowat.ch/rest-api/markets/order-book 
https://tiao.io/post/exploring-the-binance-cryptocurrency-exchange-api-orderbook/ 
'''