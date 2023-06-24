# VanHack Learning Hub Code Challenge - June 2023

## Foreign Exchange Market - Best Time to Buy and Sell Stock/Commodity

## ***<span style="color:gray">*Question 1*</span>***
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

***You must write an algorithm that uses only constant extra space.***

Example 1:
<br/>
***Input***: prices = [7,1,5,3,6,4]
<br/>
***Output***: 7
<br/>
***Explanation***: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
******


Example 2:
<br/> 
***Input*** prices = [1,2,3,4,5]
<br/>
***Output***: 4
<br/>
***Explanation***: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
******


Example 3:
<br/>
***Input***: prices = [7,6,4,3,1]
<br/>
***Output***: 0
<br/>
***Explanation***: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
******

Constraints:
<br/>
1 <= prices.length <= 3 * 104
<br/>
0 <= prices[i] <= 104
<br/>
<br/>
Source: [Leetcode 122 - Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/).
******
******
<br/>

## ***<span style="color:gray">*Question 2*</span>***
You are a developer stock broker for your company and the market projection team have given you a projection of the prices of the stock/commodity for a given period of time. For example, **prices = [ 12, 9, 5, 31, 90, 3 ]**, each index represents a day and the value at each index represents the price for the day. As an important member of the company, you have been tasked to write a method to determine whether to ***buy or sell and HOLD*** (to 'HOLD' means to retain the position i.e. buy/sell taken for a period of time) a commodity/stock to maximize profit. 
<br/>
The expected return statement is "A '**sell/buy**' position should be taken on day **dayToSell/dayToBuy** and closed on **dayToClose** to get a maximum profit of maxProfit.". If the profit from taking a buy position and a sell position are same, take the trade with the earliest time to profit. If no profit can be gotten, the return the string **"No trades possible."**
<br/>

Example 1:
<br/>
***Input***: tradeList_1 = [ 7, 1, 5, 3, 6, 4 ] 
<br/>
***Output***: "A 'sell' position should be taken on day 1 and closed on day 2 to get a maximum profit of 6."
<br/>
******
<br/>

Example 2:
<br/>
***Input***: tradeList_2 = [ 1, 2, 3, 4, 5 ]
<br/>
***Output***: "A 'buy' position should be taken on day 1 and closed on day 5 to get a maximum profit of 4."
******
<br/>

Example 3:
<br/>
***Input***: tradeList_3 = [ 2, 2, 2, 2, 2 ]
<br/>
***Output***: "No trades possible."
******
<br/>

Example 4:
<br/>
***Input***: tradeList_4 = [ 4, 6, 3, 5, 1, 7 ]
<br/>
***Output***: "A 'buy' position should be taken on day 5 and closed on day 6 to get a maximum profit of 6."
******
<br/>

Example 5:
<br/>
***Input***: tradeList_5 = [ ]
<br/>
***Output***: "No trades possible."
******
<br/>

Example 6:
<br/>
***Input***: tradeList_4 = [ 1, 7, 5, 3, 7, 1 ]
<br/>
***Output***: "A 'buy' position should be taken on day 1 and closed on day 2 to get a maximum profit of 6."
******
<br/>

Example 7:
<br/>
***Input***: tradeList_4 = [ 7, 1, 5, 3, 1, 7 ]
<br/>
***Output***: "A 'sell' position should be taken on day 1 and closed on day 2 to get a maximum profit of 6."
******
<br/>

Example 8:
<br/>
***Input***: tradeList_4 = [ 4, 6, 3, -5, 1, 7 ]
<br/>
***Output***: "A 'buy' position should be taken on day 4 and closed on day 6 to get a maximum profit of 12."
<br/>
******
******


### ***You may decide to take a different path in designing and implementing your solution. Happy coding.***

***[VanHack Learning Hub](https://vanhack.com/learning-hub)***