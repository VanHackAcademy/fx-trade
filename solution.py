class Trading:
  def __init__(self):
    pass


  # Question 1 Solution
  def maxBuyProfit(self, prices: list[int]) -> int:
    """
    An analysis of the question gives a clear picture that the "Trader" is a "day Trader" looking to only buy a commodity, hence only comparative prices which favours a buy option would be considered in the method.
    """
    profit = 0

    for i in range(1, len(prices)):
      if prices[i] > prices[i - 1]:
        profit += (prices[i] - prices[i - 1])

    return profit
  

  # Question 1 Bonus Solution
  def maxSellProfit(self, prices: list[int]) -> int:
    """
    From the question, we have generated an algorithm which helps "day traders" to take buy positions. In this method, we are going to also generate an algorithm for "day traders" who are also looking out for only sell positions.
    """
    profit = 0
    prices = prices[::-1]
    for i in range(1, len(prices)):
      if prices[i] < prices[i - 1]:
        profit += (prices[i - 1] - prices[i])

    return profit
  
  
  # Question 2 Helper Method
  def maxBuyHoldProfit(self, prices: list[int]) -> str:
    maxHoldProfit = 0
    maxTrack = 0
    dayToBuy = 0
    dayToClose = 0
    for i in range(0, len(prices)):
      for k in range(i + 1, len(prices)):
        if prices[i] < prices[k]:
          maxTrack = max(maxTrack, (prices[k] - prices[i]))
        if maxTrack >  maxHoldProfit:
          maxHoldProfit = maxTrack
          dayToBuy = i + 1
          dayToClose = k + 1

    return {
      "maxHoldProfit" : maxHoldProfit,
      "dayToBuy" : dayToBuy,
      "dayToClose" : dayToClose,
    }


  # Question 2 Helper Method
  def maxSellHoldProfit(self, prices: list[int]) -> str:
    maxHoldProfit = 0
    maxTrack = 0
    dayToSell = 0
    dayToClose = 0
    for i in range(0, len(prices)):
      for k in range(i + 1, len(prices)):
        if prices[i] > prices[k]:
          maxTrack = max(maxTrack, (prices[i] - prices[k]))
        if maxTrack >  maxHoldProfit:
          maxHoldProfit = maxTrack
          dayToSell = i + 1
          dayToClose = k + 1

    return {
      "maxHoldProfit" : maxHoldProfit,
      "dayToSell" : dayToSell,
      "dayToClose" : dayToClose,
    }


  # Question 2 Solution
  def analyzeTrade(self, prices: list[int]) -> str:
    if len(prices) < 2:
      return "No trades possible."
    
    buyTrade = self.maxBuyHoldProfit(prices)
    sellTrade = self.maxSellHoldProfit(prices)
    
    if buyTrade["maxHoldProfit"] > sellTrade["maxHoldProfit"]: # take a buy position
      return f"A 'buy' position should be taken on day {buyTrade['dayToBuy']} and closed on day {buyTrade['dayToClose']} to get a max profit of {buyTrade['maxHoldProfit']}."
    
    if buyTrade["maxHoldProfit"] < sellTrade["maxHoldProfit"]: # take a sell position
      return f"A 'sell' position should be taken on day {sellTrade['dayToSell']} and closed on day {sellTrade['dayToClose']} to get a max profit of {sellTrade['maxHoldProfit']}."
  
    if buyTrade["maxHoldProfit"] == sellTrade["maxHoldProfit"] and buyTrade["dayToBuy"] < sellTrade["dayToSell"]: # take earliest possible buy trade time
      return f"A 'buy' position should be taken on day {buyTrade['dayToBuy']} and closed on day {buyTrade['dayToClose']} to get a max profit of {buyTrade['maxHoldProfit']}."
    
    if buyTrade["maxHoldProfit"] == sellTrade["maxHoldProfit"] and buyTrade["dayToBuy"] > sellTrade["dayToSell"]: # take earliest possible buy trade time
      return f"A 'sell' position should be taken on day {sellTrade['dayToSell']} and closed on day {sellTrade['dayToClose']} to get a max profit of {sellTrade['maxHoldProfit']}."
    
    return "No trades possible."
  
tradeList_1 = [7, 1, 5, 3, 6, 4] 
tradeList_2 = [1, 2, 3, 4, 5]
tradeList_3 = [7, 6, 4, 3, 1]
tradeList_4 = [4, 6, 3, 5, 1, 7] 
tradeList_5 = [ 2, 2, 2, 2, 2 ]
tradeList_6 = [ ]
tradeList_7 = [4, 6, 3, -5, 1, 7]

trade = Trading()

print(trade.analyzeTrade(tradeList_1))
# print(trade.analyzeTrade(tradeList_2))
# print(trade.analyzeTrade(tradeList_3))
# print(trade.analyzeTrade(tradeList_4))
# print(trade.analyzeTrade(tradeList_5))
# print(trade.analyzeTrade(tradeList_6))
# print(trade.analyzeTrade(tradeList_7))


