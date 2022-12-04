# Defi Arbitrage Bot

## Execution Steps: 
1. Determine current price of token from public order book
2. Find limit order of token on decentralized exchanges
3. Identify limit orders, to buy low and sell high (arbitrage) 

## Tools: 
Ethplorer API (Tokens), 0x API (Orderbook), 1inch API (DEX)

## Key Metrics: 
Latency of arbitrage
Successful order ratio (arbitrage order/all order)

## Expectation:
<60 second detection  
\>5% successful arbitrage orders 

## Results:
<5 second detection
0-50% successful arbitrage orders 

## Takeaway:
Arbitrage opportunity varies widely based on token
Off-chain requests have high latency overhead 

## Contributors

Xiaolei Shi, Xiaoren Yang, Surya Vengadesan